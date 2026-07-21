create table if not exists assurance.workforce_fact (
  tenant_id text not null,
  run_id text not null,
  business_date date not null,
  fact_id uuid not null default gen_random_uuid(),
  fact_type text not null,
  payload jsonb not null,
  created_at timestamptz not null default now(),
  primary key (tenant_id, business_date, fact_id)
) partition by list (tenant_id);

DO $$
DECLARE
  tenant_key text;
  year_value integer;
  tenant_table text;
  year_table text;
BEGIN
  FOREACH tenant_key IN ARRAY ARRAY['delta','ascension','mgm_lv','schneider','pepsico']
  LOOP
    tenant_table := format('workforce_fact_%s', tenant_key);
    EXECUTE format(
      'create table if not exists assurance.%I partition of assurance.workforce_fact for values in (%L) partition by range (business_date)',
      tenant_table, tenant_key
    );
    FOR year_value IN 2016..2026 LOOP
      year_table := format('%s_%s', tenant_table, year_value);
      EXECUTE format(
        'create table if not exists assurance.%I partition of assurance.%I for values from (%L) to (%L)',
        year_table, tenant_table, make_date(year_value, 1, 1), make_date(year_value + 1, 1, 1)
      );
    END LOOP;
  END LOOP;
END $$;

create index if not exists workforce_fact_type_idx on assurance.workforce_fact (tenant_id, fact_type, business_date);
create index if not exists workforce_fact_run_idx on assurance.workforce_fact (tenant_id, run_id, business_date);
