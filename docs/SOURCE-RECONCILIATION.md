# Source Reconciliation

## Authoritative inputs

- FINAL Workforce Decision Assurance constitution.
- Five project architecture specifications, P01 through P05.
- Five generated foundation packages containing the 337-object SDM scaffold.

## Reconciled mismatches

1. **Foundation prohibition versus generator objective** — the old tenant foundation manifests prohibited synthetic data. This repository preserves those packages as an immutable configuration layer and introduces separate generator manifests where synthetic generation is explicitly enabled.
2. **`mgm` versus `mgm_lv`** — `mgm_lv` is the canonical tenant key used in schemas and RLS. `mgm` remains the package/legacy folder slug.
3. **SDM configuration versus workforce facts** — UKG SDM `response.json` files remain empty structural envelopes. Generated workers, schedules, punches, totals, incidents, biometrics-derived states, and payroll records are written outside the SDM tree.
4. **Foundation-only SQL versus operational schema** — new migrations add tenant-first/year-second fact partitioning, assurance tables, generator-run metadata, forced RLS, and seed tenant rows.
5. **Generic tenant scaffolds versus specific operational requirements** — each tenant now has distinct roles, hierarchy, jurisdiction packs, scenario windows, protected invariants, Decision Passport classes, and tenant-specific fact streams.
6. **Random-looking data versus causal history** — generation uses a BLAKE2b seed hierarchy and scenario effects. Public incident windows create deterministic directional signatures.
7. **One workflow versus full lifecycle** — GitHub Actions now validates, generates, packages, attests, and optionally loads through a protected Supabase environment.
8. **Wage values** — the generator emits hours, pay-code context, and publication state, not wage or salary dollar values.
