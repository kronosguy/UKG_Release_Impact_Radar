from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


def normalize(value: Any) -> Any:
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, sort_keys=True, separators=(",", ":"))
    if value is None:
        return ""
    return value


class MultiFormatWriter:
    def __init__(self, root: Path, relative_name: str, formats: set[str]):
        self.root = root
        self.relative_name = relative_name
        self.formats = formats
        self.rows: list[dict[str, Any]] = []
        self.json_handle = None
        self.csv_handle = None
        self.csv_writer = None
        self.count = 0

    def __enter__(self) -> "MultiFormatWriter":
        if "jsonl" in self.formats:
            path = self.root / f"{self.relative_name}.jsonl"
            path.parent.mkdir(parents=True, exist_ok=True)
            self.json_handle = path.open("w", encoding="utf-8", newline="\n")
        return self

    def write(self, row: dict[str, Any]) -> None:
        if self.json_handle:
            self.json_handle.write(json.dumps(row, sort_keys=True, default=str) + "\n")
        if "csv" in self.formats:
            if self.csv_handle is None:
                path = self.root / f"{self.relative_name}.csv"
                path.parent.mkdir(parents=True, exist_ok=True)
                self.csv_handle = path.open("w", encoding="utf-8", newline="")
                self.csv_writer = csv.DictWriter(self.csv_handle, fieldnames=list(row.keys()))
                self.csv_writer.writeheader()
            assert self.csv_writer is not None
            self.csv_writer.writerow({key: normalize(value) for key, value in row.items()})
        if "parquet" in self.formats:
            self.rows.append(row)
        self.count += 1

    def __exit__(self, exc_type, exc, tb) -> None:
        if self.json_handle:
            self.json_handle.close()
        if self.csv_handle:
            self.csv_handle.close()
        if exc is None and "parquet" in self.formats and self.rows:
            import pandas as pd
            frame = pd.DataFrame([{key: normalize(value) for key, value in row.items()} for row in self.rows])
            path = self.root / f"{self.relative_name}.parquet"
            path.parent.mkdir(parents=True, exist_ok=True)
            frame.to_parquet(path, index=False)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_checksums(root: Path) -> dict[str, str]:
    checksums: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name not in {"SHA256SUMS", "RUN-MANIFEST.json"}:
            checksums[str(path.relative_to(root))] = sha256_file(path)
    lines = [f"{digest}  {name}" for name, digest in checksums.items()]
    (root / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return checksums
