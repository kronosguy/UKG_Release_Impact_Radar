from __future__ import annotations

import argparse
from pathlib import Path

from .engine import RunOptions, generate


TENANTS = ["delta", "ascension", "mgm_lv", "schneider", "pepsico"]


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="ukg-generate")
    sub = root.add_subparsers(dest="command", required=True)
    gen = sub.add_parser("generate")
    gen.add_argument("--tenant", required=True, choices=TENANTS)
    gen.add_argument("--start-year", type=int, default=2016)
    gen.add_argument("--end-year", type=int, default=2026)
    gen.add_argument("--profile", choices=["smoke", "demo", "portfolio", "custom"], default="smoke")
    gen.add_argument("--employee-count", type=int)
    gen.add_argument("--site-count", type=int)
    gen.add_argument("--root-seed", type=int, default=20260721)
    gen.add_argument("--seed-salt", default="ukg-assurance-final")
    gen.add_argument("--formats", default="jsonl,csv")
    gen.add_argument("--output-dir", type=Path, default=Path("out"))
    return root


def main() -> None:
    args = parser().parse_args()
    formats = {value.strip() for value in args.formats.split(",") if value.strip()}
    invalid = formats - {"jsonl", "csv", "parquet"}
    if invalid:
        raise SystemExit(f"Unsupported formats: {sorted(invalid)}")
    result = generate(RunOptions(
        tenant_key=args.tenant, start_year=args.start_year, end_year=args.end_year,
        profile=args.profile, employee_count=args.employee_count, site_count=args.site_count,
        root_seed=args.root_seed, seed_salt=args.seed_salt, formats=formats, output_dir=args.output_dir,
    ))
    print(result)


if __name__ == "__main__":
    main()
