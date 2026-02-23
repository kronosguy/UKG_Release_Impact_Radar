# Needs Review Queue Template (MVP)

File path:
`outputs/<tenantId>/<releaseId>/needs-review.json`

## Template
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
