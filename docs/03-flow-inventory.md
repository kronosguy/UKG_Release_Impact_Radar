# Flow Inventory (MVP)

## Flow 1: Snapshot — UKG Config Export
Trigger: Manual + Scheduled (weekly)
Actions:
- Load category list
- For each category:
  - Call API
  - Normalize objects
  - Write artifact file

## Flow 2: Ingest — Release Items
Trigger: Manual + Scheduled (weekly)
Actions:
- Pull release content source(s)
- Split into items
- Normalize fields
- Write artifact file

## Flow 3: Compute — Impact Report
Trigger: Manual + After Flow 1 + After Flow 2
Actions:
- Load latest snapshot artifacts
- Load release artifacts
- Load mappings/touchpoints.yml (stored copy)
- Apply mapping rules
- Score items
- Write:
  - impact-report.md
  - needs-review.json
  - change-log.md