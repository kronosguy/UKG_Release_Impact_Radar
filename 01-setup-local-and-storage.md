# Setup: Storage + Repo Hygiene (No Dataverse)

## Storage requirement
Because Dataverse may not be available, the MVP stores artifacts in:
- SharePoint Document Library **or**
- OneDrive for Business folder

Pick one and keep it consistent.

## Recommended folder roots
- `/ukg-release-impact-radar/snapshots/`
- `/ukg-release-impact-radar/releases/`
- `/ukg-release-impact-radar/outputs/`

## GitHub hygiene
Never commit:
- tokens
- secrets
- private tenant URLs
- exports containing employee data

Commit-safe artifacts:
- docs
- mappings
- samples
- output reports with redactions

## Suggested working practice
- Build flows using safe “sample” payloads first
- Run in TEST tenant first
- Commit only the markdown reports + change logs
