from __future__ import annotations

import json
from pathlib import Path

import yaml


def build_sdm_export(repo_root: Path, output_root: Path, tenant_key: str, display_name: str, package_slug: str) -> int:
    catalog_path = repo_root / "config" / "export-object-catalog.yaml"
    catalog = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    objects = catalog["spec"]["objects"]
    export_root = output_root / "sdm-export"
    export_root.mkdir(parents=True, exist_ok=True)
    export_config = {
        "comments": "Generated configuration scaffold only; operational history is stored outside SDM envelopes.",
        "sourceTenantId": f"synthetic_{tenant_key}_generator",
        "targetTenantId": f"{package_slug}_generated_foundation.json",
        "sourceLabel": f"{display_name} SYNTHETIC GENERATOR",
        "targetLabel": f"{display_name} SYNTHETIC GENERATOR",
        "version": "09.08",
        "fileVersion": "09.08",
        "fileUploadId": None,
        "retrieveResponsesBatch": [],
        "additionalProperties": {"tenantKey": tenant_key, "operationalDataEmbedded": False},
    }
    (export_root / "ExportConfig.json").write_text(json.dumps(export_config, indent=2) + "\n", encoding="utf-8")
    for item in objects:
        folder = export_root / item["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        payload = {
            "id": item["id"],
            "name": item["name"],
            "uniqueKey": item["unique_key"],
            "itemsRetrieveResponseDTOs": [],
            "itemsRetrieveResponses": [],
        }
        (folder / "response.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return len(objects)
