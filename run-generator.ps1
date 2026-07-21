[CmdletBinding()]
param(
    [ValidateSet("smoke", "demo", "portfolio")]
    [string]$Profile = "smoke",
    [ValidateRange(2016, 2026)]
    [int]$StartYear = 2016,
    [ValidateRange(2016, 2026)]
    [int]$EndYear = 2026,
    [string]$Formats = "jsonl",
    [long]$RootSeed = 20260721,
    [string]$OutputDirectory = "out"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $MyInvocation.MyCommand.Path)

if ($EndYear -lt $StartYear) {
    throw "EndYear must be greater than or equal to StartYear."
}

py -3.12 -m pip install --requirement requirements.txt
if ($LASTEXITCODE -ne 0) { throw "Dependency installation failed." }

py -3.12 scripts/generate_all.py `
    --profile $Profile `
    --start-year $StartYear `
    --end-year $EndYear `
    --formats $Formats `
    --root-seed $RootSeed `
    --output-dir $OutputDirectory
if ($LASTEXITCODE -ne 0) { throw "Generation failed." }

py -3.12 scripts/validate_all.py --input-dir $OutputDirectory
if ($LASTEXITCODE -ne 0) { throw "Validation failed." }

py -3.12 scripts/package_release.py --input-dir $OutputDirectory --release-dir release-assets
if ($LASTEXITCODE -ne 0) { throw "Packaging failed." }

Write-Host "Generation, validation, and packaging completed."
Write-Host "Artifacts: $(Join-Path (Get-Location) 'release-assets')"
