# Migration from Foundation Builder

The prior workflow generated only empty SDM-shaped foundation packages. This repository retains that exact compatibility contract and adds a separate operational generator.

Do not copy generated facts into SDM `response.json` files. Run the new generator workflow, consume the tenant ZIPs from GitHub Actions, and load only validated operational files through the protected Supabase job.
