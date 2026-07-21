from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

FIXED_ZIP_TIME = (2026, 1, 1, 0, 0, 0)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def deterministic_zip(source_dir: Path, archive: Path) -> None:
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as handle:
        for path in sorted(source_dir.rglob("*")):
            if not path.is_file():
                continue
            relative = Path(source_dir.name) / path.relative_to(source_dir)
            info = zipfile.ZipInfo(str(relative).replace("\\", "/"), FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            handle.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=Path("out"))
    parser.add_argument("--release-dir", type=Path, default=Path("release-assets"))
    args = parser.parse_args()
    args.release_dir.mkdir(parents=True, exist_ok=True)
    entries = []
    for manifest_path in sorted(args.input_dir.glob("*/run_*/RUN-MANIFEST.json")):
        run_dir = manifest_path.parent
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        archive = args.release_dir / f"{manifest['tenant_key']}-{manifest['run_id']}.zip"
        deterministic_zip(run_dir, archive)
        digest = sha256(archive)
        archive.with_suffix(".zip.sha256").write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
        entries.append({"tenant_key": manifest["tenant_key"], "run_id": manifest["run_id"], "archive": archive.name, "sha256": digest})
    (args.release_dir / "GENERATOR-PACKAGE-INDEX.json").write_text(json.dumps({"version": "1.0.0", "packages": entries}, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
