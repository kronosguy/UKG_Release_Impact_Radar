import json
from pathlib import Path

from generator.engine import RunOptions, generate


def test_same_seed_produces_same_file_checksums(tmp_path: Path):
    common = dict(
        tenant_key="delta", start_year=2024, end_year=2024, profile="custom",
        employee_count=2, site_count=1, root_seed=20260721,
        seed_salt="determinism", formats={"jsonl"},
    )
    first = generate(RunOptions(**common, output_dir=tmp_path / "a"))
    second = generate(RunOptions(**common, output_dir=tmp_path / "b"))
    first_manifest = json.loads((first / "RUN-MANIFEST.json").read_text(encoding="utf-8"))
    second_manifest = json.loads((second / "RUN-MANIFEST.json").read_text(encoding="utf-8"))
    assert first_manifest["checksums"] == second_manifest["checksums"]
