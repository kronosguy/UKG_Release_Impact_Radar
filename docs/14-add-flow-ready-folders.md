# Repo: Add Flow-Ready Folders (releases/ + snapshots/)

## Goal
Make the repo “flow-ready” by adding the folders your flows will write to, without committing sensitive exports.

## Rules
- `releases/` can be commit-safe **if you redact URLs/hosts**
- `snapshots/` should be treated as **NOT commit-safe** by default (config exports can still be sensitive)
- `outputs/` is commit-safe **if redacted**

## Create folders (repo root)
- `releases/`
- `snapshots/`

Add `.gitkeep` files so Git tracks the folders.

## Recommended gitignore behavior
- Keep `snapshots/` ignored (default safe)
- Allow `releases/` and `outputs/` to be committed

### Update `.gitignore` (add these lines if not present)
```gitignore
# Tenant config exports (do not commit)
snapshots/
```

## Commands (PowerShell)
```powershell
# from repo root
New-Item -ItemType Directory -Force .\releases | Out-Null
New-Item -ItemType Directory -Force .\snapshots | Out-Null

New-Item -ItemType File -Force .\releases\.gitkeep | Out-Null
New-Item -ItemType File -Force .\snapshots\.gitkeep | Out-Null

# ensure snapshots are ignored
if (-not (Select-String -Path .\.gitignore -Pattern "^snapshots/$" -Quiet)) {
  Add-Content -Path .\.gitignore -Value "`n# Tenant config exports (do not commit)`nsnapshots/`n"
}

git add -A
git commit -m "Add releases/ and snapshots/ folders (flow-ready) and ignore snapshots"
git push
```

## After push
Reply `GO`.
