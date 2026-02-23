# Storage + Run Naming Conventions (Power Automate MVP)

## Purpose
Ensure all artifacts written by flows land in predictable locations with stable naming.

## Storage root
In SharePoint or OneDrive, set a single root folder:
`/ukg-release-impact-radar/`

Under it, use these 3 roots:
- `snapshots/`
- `releases/`
- `outputs/`

## Flow 01 (Snapshot) write paths
Folder:
`snapshots/<tenantId>/<timestampZ>/`

Files:
- `<category>.json`

Example:
`snapshots/AHS-PROD/2026-02-23T18-11-03Z/timekeeping_exceptions.json`

## Flow 02 (Release ingest) write paths
Folder:
`releases/<releaseId>/`

Files:
- `release-items.json`

Example:
`releases/2026.02/release-items.json`

## Flow 03 (Compute impact) write paths
Folder:
`outputs/<tenantId>/<releaseId>/`

Files:
- `impact-report.md`
- `needs-review.json`
- `run.json`
- `change-log.md`

Example:
`outputs/AHS-PROD/2026.02/impact-report.md`

## Timestamp format
Use this exact format for folder names:
`yyyy-MM-ddTHH-mm-ssZ`

Example:
`2026-02-23T18-11-03Z`

## Commit safety
- Never commit: `snapshots/` (ignored)
- Commit-safe (if redacted): `outputs/`, `releases/`
