# UKG Release Impact Radar — Full Data Generator

This repository is the complete deterministic data-generation platform for the five locked Workforce Decision Assurance tenant overlays:

| Tenant | Canonical key | Primary project |
|---|---|---|
| MGM Resorts Las Vegas | `mgm_lv` | P01 |
| Ascension Healthcare | `ascension` | P02 |
| Delta Air Lines | `delta` | P03 |
| Schneider Electric | `schneider` | P04 |
| PepsiCo | `pepsico` | P05 |

The generator produces two intentionally separate artifact families:

1. **UKG SDM compatibility artifacts** — `ExportConfig.json` plus all 337 configuration-object directories and empty `response.json` envelopes.
2. **Synthetic operational and assurance history** — dimensions, schedules, punches, totals, incidents, qualifications, evidence envelopes, Decision Passports, worker-harm signals, payroll outbox records, tenant-specific facts, validation reports, and Supabase-ready files.

Generated operational data is never inserted into SDM configuration envelopes.

## Run locally

```bash
python -m pip install --requirement requirements.txt
python -m generator.cli generate   --tenant delta   --start-year 2016   --end-year 2026   --profile smoke   --formats jsonl,csv   --output-dir out
```

Generate all tenants:

```bash
python scripts/generate_all.py --profile smoke --start-year 2016 --end-year 2026
```

Validate an existing run:

```bash
python scripts/validate_all.py --input-dir out
```

## Profiles

- `smoke`: 4 workers per tenant; full constitutional time window; intended for CI.
- `demo`: 100 workers per tenant; interview and architecture demonstration.
- `portfolio`: tenant-sized synthetic sample controlled by each tenant manifest.
- `custom`: requires `--employee-count` and optional `--site-count`.

## GitHub Actions

The `generate-workforce-history.yml` workflow validates the control plane, creates one artifact per tenant, builds a combined release index, and can optionally load approved artifacts into Supabase through a protected environment.

## Safety boundary

The platform generates synthetic workforce history. It does not produce real wages, real identities, raw facial images, production credentials, or client production data.
