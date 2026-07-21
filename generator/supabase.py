from __future__ import annotations

import json
from pathlib import Path

import psycopg


DIMENSION_TABLE_MAP = {
    "dimensions/business_nodes.jsonl": "business_node",
    "dimensions/workers.jsonl": "worker",
    "dimensions/assignments.jsonl": "assignment",
    "dimensions/qualifications.jsonl": "qualification",
}

ASSURANCE_TABLE_MAP = {
    "assurance/evidence_envelopes.jsonl": "evidence_envelope",
    "assurance/decision_passports.jsonl": "decision_passport",
    "assurance/worker_harm_signals.jsonl": "worker_harm_signal",
}

FACT_TYPE_MAP = {
    "facts/schedules.jsonl": "work_schedule",
    "facts/punches.jsonl": "punch_event",
    "facts/timecard_totals.jsonl": "timecard_total",
    "facts/incidents.jsonl": "incident_event",
    "facts/payroll_publications.jsonl": "payroll_publication",
}


def iter_jsonl(path: Path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def load_run(run_dir: Path, database_url: str, schema: str = "assurance", apply: bool = False) -> dict[str, int]:
    if not apply:
        raise ValueError("Supabase load requires explicit apply=True")
    manifest = json.loads((run_dir / "RUN-MANIFEST.json").read_text(encoding="utf-8"))
    report = json.loads((run_dir / "VALIDATION-REPORT.json").read_text(encoding="utf-8"))
    if not manifest.get("validation_passed") or not report.get("passed"):
        raise ValueError("Run validation did not pass")

    tenant_key = manifest["tenant_key"]
    run_id = manifest["run_id"]
    counts: dict[str, int] = {}

    with psycopg.connect(database_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute("select set_config('app.tenant_id', %s, true)", (tenant_key,))
            cursor.execute("select set_config('app.role_name', 'tenant_assurance_service', true)")
            cursor.execute(
                f"insert into {schema}.generator_run (run_id, tenant_id, root_seed, start_year, end_year, profile, manifest, validation_report) "
                "values (%s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb) "
                "on conflict (run_id) do update set manifest = excluded.manifest, validation_report = excluded.validation_report",
                (run_id, tenant_key, manifest["root_seed"], manifest["start_year"], manifest["end_year"], manifest["profile"], json.dumps(manifest), json.dumps(report)),
            )

            for relative, table in {**DIMENSION_TABLE_MAP, **ASSURANCE_TABLE_MAP}.items():
                path = run_dir / relative
                if not path.exists():
                    continue
                cursor.execute(f"delete from {schema}.{table} where tenant_id = %s and run_id = %s", (tenant_key, run_id))
                loaded = 0
                for payload in iter_jsonl(path):
                    cursor.execute(
                        f"insert into {schema}.{table} (tenant_id, run_id, payload) values (%s, %s, %s::jsonb)",
                        (tenant_key, run_id, json.dumps(payload)),
                    )
                    loaded += 1
                counts[table] = loaded

            cursor.execute(f"delete from {schema}.workforce_fact where tenant_id = %s and run_id = %s", (tenant_key, run_id))
            for relative, fact_type in FACT_TYPE_MAP.items():
                path = run_dir / relative
                if not path.exists():
                    continue
                loaded = 0
                for payload in iter_jsonl(path):
                    business_date = payload.get("business_date") or payload.get("opened_at", "")[:10]
                    if not business_date:
                        raise ValueError(f"Missing business date for {relative}")
                    cursor.execute(
                        f"insert into {schema}.workforce_fact (tenant_id, run_id, business_date, fact_type, payload) values (%s, %s, %s, %s, %s::jsonb)",
                        (tenant_key, run_id, business_date, fact_type, json.dumps(payload)),
                    )
                    loaded += 1
                counts[fact_type] = loaded
        connection.commit()
    return counts
