import json
from pathlib import Path

from generator.engine import RunOptions, generate


def test_smoke_generation(tmp_path: Path):
    output = generate(RunOptions(
        tenant_key="pepsico", start_year=2023, end_year=2024, profile="smoke",
        employee_count=4, site_count=2, root_seed=20260721,
        seed_salt="test", formats={"jsonl"}, output_dir=tmp_path,
    ))
    report = json.loads((output / "VALIDATION-REPORT.json").read_text(encoding="utf-8"))
    assert report["passed"] is True
    assert report["sdm_response_count"] == 337
    assert (output / "facts/punches.jsonl").exists()
    assert (output / "tenant-specific/capture_assurance.jsonl").exists()
