# Flow 03 — Compute Impact (MVP)

## Purpose
Join latest config snapshots + normalized release items + touchpoint mapping rules, then produce:
- an impact report (ranked)
- a needs-review queue
- run metadata
- a change log entry

## Flow name
`UIR - Compute Release Impact (MVP)`

## Trigger
Manual + (optional) after Flow 01 and Flow 02 complete

### Trigger inputs (manual run)
- `tenantId` (text) — example: `AHS-PROD`
- `releaseId` (text) — example: `2026.02`

## Inputs (artifacts)

### Config snapshots folder
`snapshots/<tenantId>/<timestampZ>/`  
Contains one file per category:
- `<category>.json`

### Release items file
`releases/<releaseId>/release-items.json`

### Touchpoints mapping file
`mappings/touchpoints.yml`

## Outputs (artifacts)

### 1) Impact report (markdown)
`outputs/<tenantId>/<releaseId>/impact-report.md`

### 2) Needs review queue (json)
`outputs/<tenantId>/<releaseId>/needs-review.json`

### 3) Run metadata (json)
`outputs/<tenantId>/<releaseId>/run.json`

### 4) Change log (append-only markdown)
`outputs/<tenantId>/<releaseId>/change-log.md`

## Exposure definition (MVP)
A touchpoint is considered **exposed** if the snapshot for any matching category contains at least one object.

Example:
- touchpoint `timekeeping_exceptions` is exposed if `snapshots/.../timekeeping_exceptions.json` has `objects.length > 0`

## Mapping algorithm (MVP)
For each release item:
1. `text = lower(title + " " + description)`
2. `matchedTouchpoints = []`
3. For each touchpoint in `mappings/touchpoints.yml`:
   - If any keyword appears in `text`, add that touchpoint id
4. If `matchedTouchpoints` is empty -> route to Needs Review

## Scoring algorithm (MVP)
For each release item and each matched touchpoint:
- `criticality` = touchpoint.criticality (1-5)
- `exposure` = 1 if exposed else 0
- `score` = criticality * (exposure + 0.25)

Rollup per release item:
- `maxScore` = max(score across touchpoints)
- `label`:
  - `HIGH` if maxScore >= 6
  - `MED` if maxScore between 4 and 5.99
  - `LOW` if maxScore < 4 AND exposure=1
  - `IGNORE` if exposure=0 for all matched touchpoints
  - `REVIEW` if no matched touchpoints

## Output file formats

### impact-report.md format (MVP)
- Header: tenant + release + run timestamp
- Table columns:
  - label
  - score
  - module
  - title
  - touchpoints
  - requiresAction
  - source url (redacted allowed)

### needs-review.json format (MVP)
```json
{
  "tenantId": "AHS-PROD",
  "releaseId": "2026.02",
  "capturedAtUtc": "2026-02-23T00:00:00Z",
  "items": [
    {
      "id": "2026.02-009",
      "module": "Other",
      "title": "Unmapped item",
      "description": "Text did not match any keywords",
      "source": { "provider": "ukg", "url": "https://<release-url>" }
    }
  ]
}
```

### run.json format (MVP)
```json
{
  "tenantId": "AHS-PROD",
  "releaseId": "2026.02",
  "runAtUtc": "2026-02-23T00:00:00Z",
  "snapshotFolder": "snapshots/AHS-PROD/2026-02-23T18-11-03Z",
  "releaseFile": "releases/2026.02/release-items.json",
  "mappingFile": "mappings/touchpoints.yml",
  "outputFolder": "outputs/AHS-PROD/2026.02"
}
```

### change-log.md format (MVP)
Append-only entry per compute run:
- run timestamp
- counts: HIGH/MED/LOW/IGNORE/REVIEW
- top 5 HIGH items (titles only)

## Notes / constraints
- Deterministic rules engine (keywords first).
- “Smart” mapping can be added later, but MVP stays auditable.
- Keep artifacts public-safe; redact URLs/hosts where needed.
