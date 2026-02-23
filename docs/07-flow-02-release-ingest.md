# Flow 02 — Release Ingest (MVP)

## Purpose
Normalize UKG release content into structured “release items” so we can map them to configuration touchpoints and score impact.

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

## MVP Ingestion Sources (Pick One)

### Option A (Fast): Manual Entry Queue

Maintain a simple list of release items in a:

- JSON file  
  **or**
- SharePoint list  

Each item must include:

- `title`
- `type`
- `description`
- `module`
- `url`

The Power Automate flow:

1. Reads the list.
2. Normalizes each record.
3. Outputs the standardized release artifact.

---

### Option B (Preferred): Pull from Maintained RSS / HTML Page

1. Use **HTTP GET** to fetch release content page(s).
2. Split content into structured sections.
3. For each section:
   - Create a release item record.
4. Output the normalized release artifact.

---

## Required Normalization Rules

- `id`  
  Must be stable within a release.  
  Format: <releaseId>-NNN

- `module`  
Must be one of:
- Timekeeping  
- Scheduling  
- Absence  
- Integrations  
- Security  
- Other  

- `type`  
Must be one of:
- New  
- Enhancement  
- Fix  
- Known Issue  
- Deprecation  

- `description`  
Must be **plain text only** (no HTML).

- `url`  
Must be stored internally.  
May be redacted for public GitHub repository commits.

---

## Notes / Constraints

- Release notes are not fully machine-readable.  
MVP includes a required review pass.

- Artifacts must contain **no employee data**.  
Release items are strictly vendor-provided text.