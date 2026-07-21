# Generated Output Contract

Each run produces:

```text
<tenant>/<run_id>/
├── RUN-MANIFEST.json
├── VALIDATION-REPORT.json
├── SHA256SUMS
├── sdm-export/
│   ├── ExportConfig.json
│   └── <337 configuration object folders>/response.json
├── dimensions/
├── facts/
├── assurance/
└── tenant-specific/
```

Every output row carries a canonical `tenant_key` and stable tenant UUID. The generator does not create real identities, real wages, production credentials, or raw facial images.
