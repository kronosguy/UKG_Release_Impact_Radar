from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from generator.engine import RunOptions, generate

TENANTS = ["mgm_lv", "ascension", "delta", "schneider", "pepsico"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="smoke", choices=["smoke", "demo", "portfolio"])
    parser.add_argument("--start-year", type=int, default=2016)
    parser.add_argument("--end-year", type=int, default=2026)
    parser.add_argument("--root-seed", type=int, default=20260721)
    parser.add_argument("--seed-salt", default="ukg-assurance-final")
    parser.add_argument("--formats", default="jsonl,csv")
    parser.add_argument("--output-dir", type=Path, default=Path("out"))
    args = parser.parse_args()
    outputs = []
    for tenant in TENANTS:
        output = generate(RunOptions(
            tenant_key=tenant, start_year=args.start_year, end_year=args.end_year,
            profile=args.profile, employee_count=None, site_count=None,
            root_seed=args.root_seed, seed_salt=args.seed_salt,
            formats={value.strip() for value in args.formats.split(",") if value.strip()},
            output_dir=args.output_dir,
        ))
        outputs.append(str(output))
        print(output)
    index = {"version": "1.0.0", "outputs": outputs}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "GENERATION-INDEX.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
