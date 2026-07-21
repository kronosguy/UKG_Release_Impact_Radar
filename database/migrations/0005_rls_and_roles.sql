create or replace function authz.current_tenant_id()
returns text language sql stable as $$
  select coalesce(
    nullif(current_setting('app.tenant_id', true), ''),
    nullif(auth.jwt() -> 'app_metadata' ->> 'tenant_id', '')
  )
$$;

DO $$
DECLARE role_name text;
BEGIN
  FOREACH role_name IN ARRAY ARRAY['tenant_analyst','tenant_manager','tenant_payroll_bot','tenant_assurance_service','platform_sre_masked','break_glass_security_officer']
  LOOP
    IF NOT EXISTS (select 1 from pg_roles where rolname = role_name) THEN
      EXECUTE format('create role %I noinherit', role_name);
    END IF;
  END LOOP;
END $$;

revoke all on schema assurance from public;
revoke all on all tables in schema assurance from public;

DO $$
DECLARE table_name text;
BEGIN
  FOREACH table_name IN ARRAY ARRAY[
    'business_node','worker','assignment','qualification','workforce_fact',
    'evidence_envelope','decision_passport','worker_harm_signal','generator_run'
  ] LOOP
    EXECUTE format('alter table assurance.%I enable row level security', table_name);
    EXECUTE format('alter table assurance.%I force row level security', table_name);
    EXECUTE format('drop policy if exists tenant_isolation_%I on assurance.%I', table_name, table_name);
    EXECUTE format(
      'create policy tenant_isolation_%I on assurance.%I using (tenant_id = authz.current_tenant_id()) with check (tenant_id = authz.current_tenant_id())',
      table_name, table_name
    );
  END LOOP;
END $$;

create or replace view assurance_private.v_generator_run_masked as
select run_id, tenant_id, start_year, end_year, profile, created_at,
       jsonb_build_object('record_counts', manifest -> 'record_counts', 'validation_passed', manifest -> 'validation_passed') as manifest_masked
from assurance.generator_run;

create or replace view assurance_private.v_workforce_fact_masked as
select tenant_id, run_id, business_date, fact_type, created_at,
       payload - 'worker_id' - 'punch_id' - 'source_device_id' - 'payload_sha256' as payload_masked
from assurance.workforce_fact;

grant usage on schema assurance to tenant_analyst, tenant_manager, tenant_payroll_bot, tenant_assurance_service;
grant usage on schema assurance_private to platform_sre_masked;
grant select on assurance.business_node, assurance.worker, assurance.assignment, assurance.qualification, assurance.workforce_fact to tenant_analyst, tenant_manager, tenant_assurance_service;
grant select, insert, delete on assurance.evidence_envelope, assurance.decision_passport, assurance.worker_harm_signal, assurance.generator_run to tenant_assurance_service;
grant insert, delete on assurance.business_node, assurance.worker, assurance.assignment, assurance.qualification, assurance.workforce_fact to tenant_assurance_service;
grant select on assurance_private.v_generator_run_masked, assurance_private.v_workforce_fact_masked to platform_sre_masked;
