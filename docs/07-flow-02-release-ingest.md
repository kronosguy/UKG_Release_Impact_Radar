# Flow 02 — Release Ingest (MVP)

## Purpose
Normalize upcoming UKG release content into structured “release items” so we can map them to configuration touchpoints and score impact.

## Flow name
`UIR - Ingest Release Items (MVP)`

## Trigger
Manual + Scheduled (weekly)

### Trigger inputs (manual run)
- `releaseId` (text) — example: `2026.02`
- `publishDate` (text) — example: `2026-02-23`

## Storage (no Dataverse)
Artifacts are stored as JSON:
- `releases/<releaseId>/release-items.json`

## Artifact contract
`release-items.json`

```json
{
  "releaseId": "2026.02",
  "publishDate": "2026-02-23",
  "items": [
    {
      "id": "2026.02-001",
      "module": "Timekeeping",
      "title": "Example release item",
      "type": "Enhancement",
      "description": "Example description text.",
      "source": {
        "provider": "ukg",
        "url": "https://<release-url>"
      },
      "tags": [],
      "touchpoints": [],
      "requiresAction": false
    }
  ]
}
```

## MVP ingestion sources (pick one)

## Option A (Fast): Manual Entry Queue
Maintain a simple list of release items in a:
- JSON file **or**
- SharePoint list

Each item must include:
- `title`
- `type`
- `description`
- `module`
- `url`

The Power Automate flow:
1. Reads the list
2. Normalizes each record
3. Outputs the standardized release artifact

---

## Option B (Preferred): Pull from Maintained RSS / HTML Page
1. Use **HTTP GET** to fetch release content page(s)
2. Split content into structured sections
3. For each section:
   - Create a release item record
4. Output the normalized release artifact

---

## Required normalization rules
- `id` must be stable within a release (format: `<releaseId>-NNN`)
- `module` must be one of: `Timekeeping | Scheduling | Absence | Integrations | Security | Other`
- `type` must be one of: `New | Enhancement | Fix | Known Issue | Deprecation`
- `description` must be plain text (no HTML)
- `url` must be stored but may be redacted for public repo commits

## Notes / constraints
- Release notes are not fully machine-readable; MVP supports a review pass.
- Keep artifacts free of employee data; release items are vendor text only.
- Do not commit private tenant URLs, tokens, or internal links to GitHub.
