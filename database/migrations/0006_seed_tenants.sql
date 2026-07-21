insert into assurance.tenant (tenant_id, tenant_uuid, display_name, primary_project) values
  ('pepsico', '10000000-0000-4000-8000-000000000001', 'PepsiCo', 'P05'),
  ('ascension', '10000000-0000-4000-8000-000000000002', 'Ascension Healthcare', 'P02'),
  ('delta', '10000000-0000-4000-8000-000000000003', 'Delta Air Lines', 'P03'),
  ('mgm_lv', '10000000-0000-4000-8000-000000000004', 'MGM Resorts Las Vegas', 'P01'),
  ('schneider', '10000000-0000-4000-8000-000000000005', 'Schneider Electric', 'P04')
on conflict (tenant_id) do update set
  tenant_uuid = excluded.tenant_uuid,
  display_name = excluded.display_name,
  primary_project = excluded.primary_project;
