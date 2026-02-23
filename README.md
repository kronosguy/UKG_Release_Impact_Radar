# UKG Release Impact Radar (Power Automate)

Release management for UKG Pro WFM without the guessing.

This project snapshots tenant configuration, ingests upcoming release content, maps release changes to known configuration touchpoints, and produces an impact report that tells us what will likely change, what to validate, and what can be ignored.

## What this does (MVP)
- Pulls configuration snapshots via SDM-aligned API patterns (category-based exports)
- Normalizes snapshots into a stable JSON contract
- Ingests release items and normalizes them into a stable JSON contract
- Tags release items to configuration touchpoints
- Calculates impact score (exposure + breadth + criticality)
- Publishes outputs:
  - Impact report (markdown)
  - “Needs Review” queue (for ambiguous items)
  - Change log (what changed since last run)

## What this does NOT do (yet)
- It does not prove payroll outcomes from release notes alone.
- It does not auto-fix config.
- Regression testing comes after MVP (post-update scenario runner).

## Repo layout
- docs/ — end-to-end documentation and runbook
- mappings/ — touchpoint mapping rules (human-owned truth)
- samples/ — JSON contracts for payloads and outputs

## Operating model
- Weekly snapshot + release ingest cadence
- On-demand runs during release windows
- All outputs are committed to this repo for traceability