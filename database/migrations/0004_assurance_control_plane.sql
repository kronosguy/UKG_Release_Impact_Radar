create table if not exists assurance.evidence_envelope (
  id uuid primary key default gen_random_uuid(),
  tenant_id text not null references assurance.tenant(tenant_id),
  run_id text not null,
  payload jsonb not null,
  created_at timestamptz not null default now()
);
create table if not exists assurance.decision_passport (
  id uuid primary key default gen_random_uuid(),
  tenant_id text not null references assurance.tenant(tenant_id),
  run_id text not null,
  payload jsonb not null,
  created_at timestamptz not null default now()
);
create table if not exists assurance.worker_harm_signal (
  id uuid primary key default gen_random_uuid(),
  tenant_id text not null references assurance.tenant(tenant_id),
  run_id text not null,
  payload jsonb not null,
  created_at timestamptz not null default now()
);
create table if not exists assurance.generator_run (
  run_id text primary key,
  tenant_id text not null references assurance.tenant(tenant_id),
  root_seed bigint not null,
  start_year integer not null,
  end_year integer not null,
  profile text not null,
  manifest jsonb not null,
  validation_report jsonb not null,
  created_at timestamptz not null default now()
);
create index if not exists evidence_envelope_run_idx on assurance.evidence_envelope (tenant_id, run_id);
create index if not exists decision_passport_run_idx on assurance.decision_passport (tenant_id, run_id);
create index if not exists worker_harm_signal_run_idx on assurance.worker_harm_signal (tenant_id, run_id);
