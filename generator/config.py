from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class TenantConfig:
    tenant_key: str
    tenant_uuid: str
    package_slug: str
    display_name: str
    primary_project: str
    supporting_projects: tuple[str, ...]
    portfolio_employee_count: int
    portfolio_site_count: int
    hierarchy_levels: tuple[str, ...]
    sites: tuple[str, ...]
    roles: tuple[dict[str, Any], ...]
    jurisdiction_packs: tuple[str, ...]
    decision_passport_classes: tuple[str, ...]
    tenant_specific_stream: str


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_tenant(tenant_key: str) -> TenantConfig:
    path = REPO_ROOT / "tenants" / f"{tenant_key}.yaml"
    if not path.exists():
        raise ValueError(f"Unknown tenant: {tenant_key}")
    raw = load_yaml(path)
    meta = raw["metadata"]
    spec = raw["spec"]
    gen = spec["generator"]
    return TenantConfig(
        tenant_key=meta["tenant_key"],
        tenant_uuid=meta["tenant_uuid"],
        package_slug=meta["package_slug"],
        display_name=meta["display_name"],
        primary_project=spec["project_binding"]["primary_project"],
        supporting_projects=tuple(spec["project_binding"]["supporting_projects"]),
        portfolio_employee_count=int(gen["portfolio_employee_count"]),
        portfolio_site_count=int(gen["portfolio_site_count"]),
        hierarchy_levels=tuple(spec["hierarchy"]["levels"]),
        sites=tuple(spec["hierarchy"]["seed_sites"]),
        roles=tuple(spec["roles"]),
        jurisdiction_packs=tuple(spec["jurisdiction_packs"]),
        decision_passport_classes=tuple(spec["decision_passport_classes"]),
        tenant_specific_stream=gen["tenant_specific_stream"],
    )


def load_scenarios() -> dict[str, Any]:
    return load_yaml(REPO_ROOT / "control-plane" / "scenario-calendar.yaml")


def load_invariants() -> dict[str, Any]:
    return load_yaml(REPO_ROOT / "control-plane" / "frozen-invariants.yaml")
