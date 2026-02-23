# Repo Normalization Step (Do This Next)

## What I see (current state)
Your structure is solid. You have:
- `docs/` covering the MVP flows + templates
- `mappings/`, `samples/`, `outputs/`
- Standard repo files: `README.md`, `LICENSE`, `.gitignore`, `SECURITY.md`, `CONTRIBUTING.md`

## The problem
You have **duplicate “policy” docs** in two forms:
- Standard: `SECURITY.md` and `CONTRIBUTING.md`
- Duplicates: `02-security.md` and `03-contributing.md` (root)

This creates confusion: people won’t know which one is authoritative.

## Decision (MVP clean)
Make the **standard files authoritative**:
- KEEP: `SECURITY.md`, `CONTRIBUTING.md`
- REMOVE: `02-security.md`, `03-contributing.md`

Keep the numbered “overview” docs if you want, but they should not duplicate the standard policy files.

## One-step action
Delete the two duplicate files and commit.

### Commands (PowerShell)
```powershell
# from repo root
Remove-Item .\02-security.md -Force
Remove-Item .\03-contributing.md -Force

git add -A
git commit -m "Remove duplicate security/contributing docs; keep standard policy files"
git push
```

## After this commit
Reply `GO` and I’ll give you the next single step: add `releases/` + `snapshots/` folder placeholders and the exact Power Automate export/run artifact conventions so the repo is “flow-ready.”
