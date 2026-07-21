from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from generator.supabase import load_run


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--schema", default=os.environ.get("SUPABASE_SCHEMA", "assurance"))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    database_url = os.environ.get("SUPABASE_DB_URL")
    if not database_url:
        raise SystemExit("SUPABASE_DB_URL is required")
    print(load_run(args.run_dir, database_url, args.schema, args.apply))

if __name__ == "__main__":
    main()
