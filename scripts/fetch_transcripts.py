from __future__ import annotations

import html
import json
import os
import random
import re
import shutil
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig, WebshareProxyConfig

PLAYLIST_URL = os.environ["PLAYLIST_URL"]
OUTPUT_DIR = Path("transcripts")
LANGUAGES = [
    value.strip()
    for value in os.getenv("LANGUAGE_CODES", "en").split(",")
    if value.strip()
]
MAX_VIDEOS = int(os.getenv("MAX_VIDEOS", "0"))
FAIL_ON_PARTIAL = os.getenv("FAIL_ON_PARTIAL", "false").lower() == "true"
COOKIE_FILE = os.getenv("YOUTUBE_COOKIES_FILE", "").strip()
USER_AGENT = os.getenv("YOUTUBE_USER_AGENT", "").strip()
RETRIES = 3

TERMINAL_API_ERRORS = {
    "AgeRestricted",
    "InvalidVideoId",
    "NoTranscriptFound",
    "PoTokenRequired",
    "TranscriptsDisabled",
    "VideoUnavailable",
    "VideoUnplayable",
}
BLOCK_MARKERS = (
    "requestblocked",
    "ipblocked",
    "sign in to confirm you",
    "not a bot",
    "cloud provider",
    "requests from your ip",
    "http error 429",
    "too many requests",
)


def clean_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"<[^>]+>", "", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_error(error: BaseException, limit: int = 1400) -> str:
    value = str(error).strip().replace("\r", "")
    return value if len(value) <= limit else value[: limit - 3] + "..."


def safe_filename(title: str, video_id: str, index: int) -> str:
    title = re.sub(r'[\\/*?:"<>|\x00-\x1f]', "", html.unescape(title))
    title = re.sub(r"\s+", " ", title).strip(" .")[:140] or f"video-{video_id}"
    return f"{index:03d}_{title}__{video_id}.md"


def timestamp(seconds: float) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    seconds, milliseconds = divmod(milliseconds, 1000)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
    return f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"


def proxy_settings():
    username = os.getenv("WEBSHARE_PROXY_USERNAME", "").strip()
    password = os.getenv("WEBSHARE_PROXY_PASSWORD", "").strip()
    generic = os.getenv("TRANSCRIPT_PROXY_URL", "").strip()

    if bool(username) != bool(password):
        raise RuntimeError("Both Webshare proxy secrets must be configured together.")

    if username:
        locations = [
            value.strip().lower()
            for value in os.getenv("WEBSHARE_PROXY_LOCATIONS", "us").split(",")
            if value.strip()
        ]
        return (
            WebshareProxyConfig(
                proxy_username=username,
                proxy_password=password,
                filter_ip_locations=locations or None,
            ),
            "webshare",
        )

    if generic:
        return (
            GenericProxyConfig(http_url=generic, https_url=generic),
            "generic",
        )

    return None, "none"


def access_strategy(proxy_mode: str) -> str:
    parts: list[str] = []
    if proxy_mode != "none":
        parts.append(proxy_mode)
    if COOKIE_FILE:
        parts.append("cookies")
    if os.getenv("RUNNER_ENVIRONMENT", "").lower() == "self-hosted":
        parts.append("self-hosted")
    return "+".join(parts) or "unauthenticated-cloud"


def ydl_options(*, playlist: bool = False, ignore_errors: bool = False) -> dict[str, Any]:
    options: dict[str, Any] = {
        "quiet": True,
        "no_warnings": False,
        "ignoreerrors": ignore_errors,
        "retries": 5,
        "extractor_retries": 5,
        "socket_timeout": 30,
        "noplaylist": not playlist,
        "js_runtimes": {"node": {"path": shutil.which("node")}},
    }

    proxy = (
        os.getenv("YT_DLP_PROXY", "").strip()
        or os.getenv("TRANSCRIPT_PROXY_URL", "").strip()
    )
    if proxy:
        options["proxy"] = proxy

    if COOKIE_FILE:
        options["cookiefile"] = COOKIE_FILE

    if USER_AGENT:
        options["http_headers"] = {
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-US,en;q=0.9",
        }

    return options


def playlist_entries() -> list[dict[str, Any]]:
    options = ydl_options(playlist=True, ignore_errors=True)
    options.update({"extract_flat": "in_playlist", "skip_download": True})
    if MAX_VIDEOS > 0:
        options["playlistend"] = MAX_VIDEOS

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(PLAYLIST_URL, download=False)

    entries = (
        []
        if not info
        else [
            entry
            for entry in info.get("entries", [])
            if entry and entry.get("id")
        ]
    )
    if not entries:
        raise RuntimeError("No usable playlist entries were retrieved.")
    return entries


def api_transcript(api: YouTubeTranscriptApi, video_id: str):
    last_error: BaseException | None = None

    for attempt in range(1, RETRIES + 1):
        try:
            transcript = api.fetch(video_id, languages=LANGUAGES)
            segments = [
                (float(item.start), clean_text(item.text))
                for item in transcript.snippets
                if clean_text(item.text)
            ]
            if not segments:
                raise RuntimeError("The transcript API returned no text.")
            language = str(
                getattr(transcript, "language_code", LANGUAGES[0])
            )
            return segments, language, "youtube-transcript-api"
        except Exception as error:
            last_error = error
            if error.__class__.__name__ in TERMINAL_API_ERRORS:
                break
            if attempt < RETRIES:
                delay = min(8.0, 2 ** (attempt - 1) + random.random())
                print(
                    f"  API attempt {attempt} failed; "
                    f"retrying in {delay:.1f}s"
                )
                time.sleep(delay)

    if last_error is None:
        raise RuntimeError("Transcript retrieval failed without an error.")
    raise last_error


def language_match(candidate: str, preferred: str) -> bool:
    candidate = candidate.lower()
    preferred = preferred.lower()
    return (
        candidate == preferred
        or candidate.startswith(preferred + "-")
        or preferred.startswith(candidate + "-")
    )


def select_track(info: dict[str, Any]):
    sources = (
        ("manual", info.get("subtitles") or {}),
        ("automatic", info.get("automatic_captions") or {}),
    )

    for preferred in LANGUAGES:
        for source, tracks in sources:
            for language in tracks:
                if (
                    language != "live_chat"
                    and language_match(language, preferred)
                ):
                    return source, language

    for source, tracks in sources:
        candidates = [
            language
            for language in tracks
            if language != "live_chat"
        ]
        if candidates:
            original = [
                language
                for language in candidates
                if language.endswith("-orig")
            ]
            return source, original[0] if original else sorted(candidates)[0]

    return None


def ytdlp_transcript(video_id: str):
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    with yt_dlp.YoutubeDL(
        {
            **ydl_options(ignore_errors=False),
            "skip_download": True,
        }
    ) as ydl:
        info = ydl.extract_info(video_url, download=False)

    if not info:
        raise RuntimeError("yt-dlp could not inspect the video.")

    selected = select_track(info)
    if not selected:
        raise RuntimeError(
            "No manual subtitle or automatic-caption track exists."
        )

    source, language = selected

    with tempfile.TemporaryDirectory(
        prefix=f"captions-{video_id}-"
    ) as temp_dir:
        options = ydl_options(ignore_errors=False)
        options.update(
            {
                "skip_download": True,
                "writesubtitles": source == "manual",
                "writeautomaticsub": source == "automatic",
                "subtitleslangs": [language],
                "subtitlesformat": "json3",
                "outtmpl": str(Path(temp_dir) / "%(id)s.%(ext)s"),
                "overwrites": True,
            }
        )

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.extract_info(video_url, download=True)

        files = sorted(Path(temp_dir).glob(f"{video_id}.*.json3"))
        if not files:
            raise RuntimeError(
                "yt-dlp found captions but did not download JSON3 output."
            )

        data = json.loads(files[0].read_text(encoding="utf-8"))

    segments = []
    for event in data.get("events", []):
        text = clean_text(
            "".join(
                segment.get("utf8", "")
                for segment in event.get("segs", [])
            )
        )
        if text:
            segments.append(
                (float(event.get("tStartMs", 0)) / 1000.0, text)
            )

    if not segments:
        raise RuntimeError("yt-dlp downloaded an empty caption track.")

    return segments, language, f"yt-dlp-{source}"


def is_infrastructure_block(error: BaseException) -> bool:
    value = (
        f"{error.__class__.__name__}: {error}"
        .lower()
        .replace("\r", "")
    )
    return any(marker in value for marker in BLOCK_MARKERS)


def write_transcript(
    path: Path,
    title: str,
    video_id: str,
    language: str,
    source: str,
    segments,
):
    lines = [
        f"# {title}",
        "",
        f"- **Video:** https://www.youtube.com/watch?v={video_id}",
        f"- **Video ID:** `{video_id}`",
        f"- **Language:** `{language}`",
        f"- **Retrieval source:** `{source}`",
        "",
        "## Transcript",
        "",
    ]
    lines.extend(
        f"**{timestamp(start)}** {text}"
        for start, text in segments
    )
    path.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


def write_reports(
    results: list[dict[str, Any]],
    proxy_mode: str,
    strategy: str,
):
    success = sum(
        item["status"] == "success"
        for item in results
    )
    failed = sum(
        item["status"] == "failed"
        for item in results
    )
    skipped = sum(
        item["status"] == "skipped"
        for item in results
    )

    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "playlist_url": PLAYLIST_URL,
        "requested_languages": LANGUAGES,
        "access_strategy": strategy,
        "proxy_mode": proxy_mode,
        "cookies_configured": bool(COOKIE_FILE),
        "total_videos": len(results),
        "successful_videos": success,
        "failed_videos": failed,
        "skipped_videos": skipped,
        "results": results,
    }
    (OUTPUT_DIR / "_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    summary = [
        "# Playlist Transcript Run",
        "",
        f"- Total videos: **{len(results)}**",
        f"- Successful: **{success}**",
        f"- Failed: **{failed}**",
        f"- Skipped: **{skipped}**",
        f"- Access strategy: **{strategy}**",
        "",
        "| # | Status | Video | Source | Language |",
        "|---:|---|---|---|---|",
    ]

    for item in results:
        title = item["title"].replace("|", "\\|")
        summary.append(
            f"| {item['index']} | {item['status']} | "
            f"{title} (`{item['video_id']}`) | "
            f"{item.get('source', '')} | "
            f"{item.get('language', '')} |"
        )

    summary_text = "\n".join(summary).rstrip() + "\n"
    (OUTPUT_DIR / "_summary.md").write_text(
        summary_text,
        encoding="utf-8",
    )

    failures = [
        item
        for item in results
        if item["status"] != "success"
    ]
    failure_lines = ["# Transcript Failures", ""]

    for item in failures:
        failure_lines.extend(
            [
                f"## {item['index']}. {item['title']}",
                "",
                f"- Status: `{item['status']}`",
                f"- Video: {item['url']}",
                "",
                "```text",
                item.get("error", "Unknown error").replace(
                    "```",
                    "[fence]",
                ),
                "```",
                "",
            ]
        )

    if not failures:
        failure_lines.append("No failures.")

    (OUTPUT_DIR / "_failures.md").write_text(
        "\n".join(failure_lines).rstrip() + "\n",
        encoding="utf-8",
    )

    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(
            os.environ["GITHUB_STEP_SUMMARY"],
            "a",
            encoding="utf-8",
        ) as handle:
            handle.write(summary_text)

    return success, failed, skipped


def main() -> int:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    results: list[dict[str, Any]] = []
    proxy_mode = "configuration-error"
    strategy = "configuration-error"

    try:
        proxy_config, proxy_mode = proxy_settings()
        strategy = access_strategy(proxy_mode)
        print(f"Access strategy: {strategy}")

        entries = playlist_entries()
        print(f"Playlist videos discovered: {len(entries)}")

        api = YouTubeTranscriptApi(proxy_config=proxy_config)

        for index, entry in enumerate(entries, start=1):
            video_id = str(entry["id"])
            title = str(
                entry.get("title")
                or f"Unknown Video {video_id}"
            )
            url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"[{index}/{len(entries)}] {title}")

            primary_error: BaseException | None = None
            fallback_error: BaseException | None = None

            try:
                try:
                    segments, language, source = api_transcript(
                        api,
                        video_id,
                    )
                except Exception as error:
                    primary_error = error
                    print(
                        "  Primary failed "
                        f"({error.__class__.__name__}); "
                        "trying yt-dlp fallback"
                    )
                    try:
                        segments, language, source = ytdlp_transcript(
                            video_id
                        )
                    except Exception as fallback:
                        fallback_error = fallback
                        raise RuntimeError(
                            "Primary: "
                            f"{error.__class__.__name__}: "
                            f"{clean_error(error)}\n\n"
                            "Fallback: "
                            f"{fallback.__class__.__name__}: "
                            f"{clean_error(fallback)}"
                        ) from fallback

                filename = safe_filename(
                    title,
                    video_id,
                    index,
                )
                write_transcript(
                    OUTPUT_DIR / filename,
                    title,
                    video_id,
                    language,
                    source,
                    segments,
                )
                results.append(
                    {
                        "index": index,
                        "video_id": video_id,
                        "title": title,
                        "url": url,
                        "status": "success",
                        "source": source,
                        "language": language,
                        "output_file": filename,
                        "segment_count": len(segments),
                    }
                )
                print(
                    f"  Success: {source}, {language}, "
                    f"{len(segments)} segments"
                )
            except Exception as error:
                results.append(
                    {
                        "index": index,
                        "video_id": video_id,
                        "title": title,
                        "url": url,
                        "status": "failed",
                        "error": clean_error(error),
                    }
                )
                print(f"  Failed: {error}")

                infrastructure_block = (
                    primary_error is not None
                    and fallback_error is not None
                    and is_infrastructure_block(primary_error)
                    and is_infrastructure_block(fallback_error)
                )

                if infrastructure_block and not any(
                    item["status"] == "success"
                    for item in results
                ):
                    reason = (
                        "Remaining videos were not attempted because "
                        "both providers confirmed an environment-wide "
                        "YouTube access block. Configure a rotating "
                        "residential proxy, a valid encrypted cookie "
                        "secret for yt-dlp, or a trusted self-hosted "
                        "runner."
                    )
                    print(f"  Fast-fail: {reason}")
                    for skipped_index, skipped_entry in enumerate(
                        entries[index:],
                        start=index + 1,
                    ):
                        skipped_id = str(skipped_entry["id"])
                        skipped_title = str(
                            skipped_entry.get("title")
                            or f"Unknown Video {skipped_id}"
                        )
                        results.append(
                            {
                                "index": skipped_index,
                                "video_id": skipped_id,
                                "title": skipped_title,
                                "url": (
                                    "https://www.youtube.com/watch?v="
                                    f"{skipped_id}"
                                ),
                                "status": "skipped",
                                "error": reason,
                            }
                        )
                    break

            if index < len(entries):
                time.sleep(1.5)

    except Exception as error:
        results.append(
            {
                "index": 0,
                "video_id": "playlist",
                "title": "Playlist retrieval",
                "url": PLAYLIST_URL,
                "status": "failed",
                "error": clean_error(error),
            }
        )

    success, failed, skipped = write_reports(
        results,
        proxy_mode,
        strategy,
    )
    print(
        f"Completed: {success} succeeded, "
        f"{failed} failed, {skipped} skipped"
    )

    if success == 0:
        print(
            "No transcripts were generated. The workflow now "
            "requires a working YouTube access strategy when "
            "GitHub-hosted IPs are blocked.",
            file=sys.stderr,
        )
        return 1

    return 1 if FAIL_ON_PARTIAL and (failed or skipped) else 0


if __name__ == "__main__":
    raise SystemExit(main())
