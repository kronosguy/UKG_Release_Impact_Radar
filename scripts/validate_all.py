from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=Path("out"))
    args = parser.parse_args()
    manifests = list(args.input_dir.glob("*/run_*/RUN-MANIFEST.json"))
    if not manifests:
        raise SystemExit("No run manifests found")
    failed = []
    for manifest_path in manifests:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        report = json.loads((manifest_path.parent / "VALIDATION-REPORT.json").read_text(encoding="utf-8"))
        print(f"{manifest['tenant_key']}: {'PASS' if report['passed'] else 'FAIL'}")
        if not report["passed"]:
            failed.append(manifest["tenant_key"])
    if failed:
        raise SystemExit(f"Validation failed: {failed}")

if __name__ == "__main__":
    main()
