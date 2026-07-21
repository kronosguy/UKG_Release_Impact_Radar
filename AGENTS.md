# Repository Execution Contract

1. The FINAL constitution in `docs/constitution/` is the governing source of truth.
2. Preserve all 337 UKG SDM object directories. Configuration exports and workforce facts are different artifact classes.
3. Never place generated workers, punches, schedules, payroll facts, biometric events, or incident history inside UKG SDM `response.json` envelopes.
4. Every consequential generated event must be reproducible from the documented seed hierarchy.
5. Every change must preserve tenant isolation, year-range validation, frozen-invariant gates, and deterministic checksums.
6. Generated outputs contain synthetic identifiers only. Never ingest or copy production employee data.
7. Supabase load is opt-in, environment-gated, and separate from generation.
8. Return complete-file replacements for changes.
9. Run `pytest`, generator smoke tests, JSON/YAML validation, and SQLFluff before completion.
10. Use conventional commits.
