# Power Automate Export + Versioning (MVP)

## Goal
Keep this repo reproducible by storing **flow exports** and **run artifacts** in a consistent, audit-safe way.

## What to store in GitHub (commit-safe)
- Docs (`docs/`)
- Mapping rules (`mappings/`)
- Samples (`samples/`)
- Outputs (`outputs/`) **only if redacted**
- Flow export packages (`flows/exports/`) **only if they contain no secrets**

## What NOT to store in GitHub
- Tenant config exports (`snapshots/`) — keep ignored
- Any file containing tokens, tenant hostnames, or employee data

## Add this folder
Create:
- `flows/exports/`

Add:
- `flows/exports/.gitkeep`

## Exporting flows (manual)
For each flow:
1. Power Automate → **My flows**
2. Select flow → **Export** → **Package (.zip)**
3. Export settings:
   - **Environment variables**: keep as references (do not embed secrets)
   - **Connections**: select “create new” on import (do not embed tokens)
4. Rename the zip using this format:
   - `UIR-Flow01-SnapshotConfig-MVP.zip`
   - `UIR-Flow02-IngestReleaseItems-MVP.zip`
   - `UIR-Flow03-ComputeReleaseImpact-MVP.zip`

Place the zips here:
- `flows/exports/`

## Repo commit checklist (before pushing)
- Zip file names follow the naming format above
- No secrets in any exported JSON inside the zip
- URLs redacted as `https://<tenant-host>` where applicable
- Outputs contain no internal hosts or employee data

## Git commands (PowerShell)
```powershell
# from repo root
New-Item -ItemType Directory -Force .\flows\exports | Out-Null
New-Item -ItemType File -Force .\flows\exports\.gitkeep | Out-Null

git add -A
git commit -m "Add flows export/versioning structure"
git push
```

## After this commit
Reply `GO` and we’ll lock in Flow 02 implementation details (manual queue option first) in a single new doc.
