# Supabase Deployment

Generation and loading are separate trust boundaries.

1. Generate and validate artifacts without credentials.
2. Review the validation report and checksums.
3. Approve the protected `supabase-production` GitHub environment.
4. The load job applies migrations in numeric order.
5. The loader sets `app.tenant_id` for each run and inserts only validated rows.
6. Forced RLS prevents cross-tenant use of base tables.

Required secret:

```text
SUPABASE_DB_URL
```

The loader requires the explicit `--apply` flag and refuses runs whose validation report did not pass.
