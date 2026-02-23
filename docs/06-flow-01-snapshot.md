# Flow 01 — Snapshot Config (MVP)

## Purpose
Create a repeatable snapshot of UKG Pro WFM configuration by category, store artifacts as JSON, and establish a baseline for impact scoring.

## Flow name
`UIR - Snapshot Config (MVP)`

## Trigger
Manual (instant cloud flow)

### Trigger inputs
- `tenantId` (text) — example: `AHS-PROD`
- `environment` (text) — example: `PROD`

## Variables
- `varCapturedAtUtc` (string) = `utcNow()`
- `varCategories` (array) = the category list used for snapshotting
- `varBaseUrl` (string) = `https://<tenant-host>`
- `varBearerToken` (string) = temporary for MVP (replace with proper auth later)

### Category list (MVP)
```json
[
  "access_method_profiles",
  "timekeeping_exceptions",
  "scheduling_zones",
  "attestation",
  "integrations_api"
]
```

## Run folder convention
`snapshots/<tenantId>/<timestampZ>/`

Example:
`snapshots/AHS-PROD/2026-02-23T18-11-03Z/`

## Inputs
- UKG base URL: `https://<tenant-host>`
- Bearer token (MVP only): stored in `varBearerToken`
- Category list: `varCategories`

## Outputs (artifacts)
One JSON file per category, written to the run folder:
- `snapshots/<tenantId>/<timestampZ>/<category>.json`

Example:
- `snapshots/AHS-PROD/2026-02-23T18-11-03Z/timekeeping_exceptions.json`

## Actions (step-by-step)
### 1) Initialize variables
Create these actions in order:
- Initialize variable `varCapturedAtUtc` (String) = `utcNow()`
- Initialize variable `varCategories` (Array) = (Category list above)
- Initialize variable `varBaseUrl` (String) = `https://<tenant-host>`
- Initialize variable `varBearerToken` (String) = `<TEMP_TOKEN>`

### 2) Compose run folder path
Action: **Compose**  
Name: `cmpRunFolder`  
Value:
`concat('snapshots/', triggerBody()?['tenantId'], '/', formatDateTime(variables('varCapturedAtUtc'),'yyyy-MM-ddTHH-mm-ssZ'))`

### 3) Loop categories
Action: **Apply to each**  
Input: `variables('varCategories')`

Inside the loop:

#### 3.1) HTTP GET category payload (placeholder endpoint)
Action: **HTTP**  
Method: `GET`  
URI: `concat(variables('varBaseUrl'), '/api/config/', items('Apply_to_each'))`

Headers:
- `Authorization` = `concat('Bearer ', variables('varBearerToken'))`
- `Accept` = `application/json`

> NOTE: `/api/config/<category>` is a placeholder. Replace with real UKG endpoints once validated.

#### 3.2) Normalize to snapshot contract
Action: **Compose**  
Name: `cmpSnapshotJson`  
Value:
```json
{
  "tenantId": "@{triggerBody()?['tenantId']}",
  "capturedAtUtc": "@{variables('varCapturedAtUtc')}",
  "category": "@{items('Apply_to_each')}",
  "objects": "@{body('HTTP')}"
}
```

#### 3.3) Write artifact file
Action: **Create file** (SharePoint or OneDrive)

Folder path:
`/ukg-release-impact-radar/@{outputs('cmpRunFolder')}`

File name:
`@{concat(items('Apply_to_each'),'.json')}`

File content:
`@{string(outputs('cmpSnapshotJson'))}`

## Normalized snapshot contract
```json
{
  "tenantId": "<tenantId>",
  "capturedAtUtc": "<utc timestamp>",
  "category": "<category>",
  "objects": []
}
```

## Notes / constraints
- Snapshot configuration only. No employee data.
- Do not commit tokens, URLs, or sensitive exports to GitHub.
- Replace placeholder endpoints + token handling after MVP.
