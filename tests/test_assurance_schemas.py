import json
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from generator.assurance import decision_passport, evidence_envelope
from generator.config import REPO_ROOT


def test_generated_assurance_records_match_final_schemas():
    occurred = datetime(2024, 7, 19, 12, 0, tzinfo=timezone.utc).isoformat()
    evidence = evidence_envelope("delta", "evt_test", "test", occurred, {"state": "manual"})
    passport = decision_passport("delta", "P03", "manual_crew_reconstruction", "employee", "wrk_test", occurred, evidence, ["DELTA-PAY-001"], "correct", [])
    pairs = [
        (evidence, "evidence-envelope.schema.json"),
        (passport, "decision-passport.schema.json"),
    ]
    for payload, schema_name in pairs:
        schema = json.loads((REPO_ROOT / "control-plane" / "schemas" / schema_name).read_text(encoding="utf-8"))
        errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(payload))
        assert errors == []
