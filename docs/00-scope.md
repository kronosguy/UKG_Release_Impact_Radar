# Scope

## Goal
Reduce time spent interpreting UKG Pro WFM releases by converting release content into a tenant-specific impact report.

## Inputs
- Tenant configuration snapshots (API-derived)
- Release items (normalized from UKG release content)
- Touchpoint mapping rules (mappings/touchpoints.yml)

## Outputs
- Impact report (ranked)
- Needs-review queue (items that cannot be confidently mapped)
- Change log (diff summary between snapshots)

## Non-goals (MVP)
- No regression testing harness
- No automated remediation
- No “perfect prediction”