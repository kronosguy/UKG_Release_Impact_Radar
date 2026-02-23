# Repo Overview

This repo documents and implements an MVP “UKG Release Impact Radar” built in Power Automate.

## What you’re building
A deterministic system that:
1. Snapshots UKG Pro WFM configuration (by category)
2. Normalizes upcoming release content into “release items”
3. Maps release items to configuration touchpoints (keyword + hint rules)
4. Scores impact (exposure + criticality)
5. Produces artifacts you can commit for auditability

## MVP limitations
- Not a perfect predictor
- Not regression testing (yet)
- Mapping requires a human “review” loop for unmapped items

## Folder layout
- `docs/` — process + flow documentation
- `mappings/` — keyword rules that drive mapping/scoring
- `samples/` — example JSON payload contracts
- `outputs/` — generated reports/artifacts (commit safe-only)
- `snapshots/` — config exports (do not commit if sensitive)
- `releases/` — normalized release items (commit safe-only)

## Flow set
- Flow 01: Snapshot config
- Flow 02: Ingest release items
- Flow 03: Compute impact and write report artifacts
