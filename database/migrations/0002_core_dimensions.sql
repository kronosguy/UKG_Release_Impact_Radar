create table if not exists assurance.tenant (
  tenant_id text primary key,
  tenant_uuid uuid not null unique,
  display_name text not null,
  primary_project text not null check (primary_project in ('P01','P02','P03','P04','P05')),
  created_at timestamptz not null default now()
);

create table if not exists assurance.business_node (
  id uuid primary key default gen_random_uuid(),
  tenant_id text not null references assurance.tenant(tenant_id),
  run_id text not null,
  payload jsonb not null,
  created_at timestamptz not null default now()
);

create table if not exists assurance.worker (
  id uuid primary key default gen_random_uuid(),
  tenant_id text not null references assurance.tenant(tenant_id),
  run_id text not null,
  payload jsonb not null,
  created_at timestamptz not null default now()
);

create table if not exists assurance.assignment (
  id uuid primary key default gen_random_uuid(),
  tenant_id text not null references assurance.tenant(tenant_id),
  run_id text not null,
  payload jsonb not null,
  created_at timestamptz not null default now()
);

create table if not exists assurance.qualification (
  id uuid primary key default gen_random_uuid(),
  tenant_id text not null references assurance.tenant(tenant_id),
  run_id text not null,
  payload jsonb not null,
  created_at timestamptz not null default now()
);

create index if not exists business_node_run_idx on assurance.business_node (tenant_id, run_id);
create index if not exists worker_run_idx on assurance.worker (tenant_id, run_id);
create index if not exists assignment_run_idx on assurance.assignment (tenant_id, run_id);
create index if not exists qualification_run_idx on assurance.qualification (tenant_id, run_id);
