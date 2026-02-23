# Security

## Never commit
- UKG tokens / refresh tokens
- Client secrets
- API keys
- Tenant URLs that expose internal routing
- Any export containing employee PII

## Redaction standard
- Replace tenant hosts with `https://<tenant-host>`
- Replace IDs with `xxxxx` unless the ID is a non-sensitive config object
- Keep payload structure intact so examples stay useful