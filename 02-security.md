# Security Rules

## Never commit
- UKG access tokens / refresh tokens
- Client secrets
- API keys
- Tenant URLs that expose internal routing
- Any export containing employee PII

## Redaction standard
- Replace tenant host with `https://<tenant-host>`
- Replace IDs with `xxxxx` unless non-sensitive config IDs
- Keep payload structure intact so examples remain useful

## Storage controls
- Store tokens in Key Vault or PA connections (future)
- For MVP, use environment variables + secure inputs (not repo)
