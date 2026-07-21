from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Any

from .seeds import stable_id


def payload_hash(payload: dict[str, Any]) -> str:
    import json
    return hashlib.sha256(json.dumps(payload, sort_keys=True, default=str).encode("utf-8")).hexdigest()


def evidence_envelope(tenant_key: str, event_id: str, source: str, occurred_at: str, payload: dict[str, Any], channel: str = "derived") -> dict[str, Any]:
    received_at = occurred_at
    return {
        "schema_version": "1.0.0",
        "envelope_id": stable_id("ee", tenant_key, event_id),
        "tenant_id": tenant_key,
        "received_at": received_at,
        "source": {"system": source, "channel": channel, "message_id": event_id, "replay_of": None},
        "payload_sha256": payload_hash(payload),
        "provenance": {"signature_state": "not_applicable", "clock_state": "derived", "device_attestation": None},
        "evidence_corruption_checks": [
            {"mode": "filtering", "result": "clear"},
            {"mode": "entanglement", "result": "clear"},
            {"mode": "construction", "result": "clear"},
            {"mode": "performance", "result": "clear"},
        ],
    }


def decision_passport(
    tenant_key: str,
    project_id: str,
    decision_class: str,
    subject_kind: str,
    subject_id: str,
    occurred_at: str,
    evidence: dict[str, Any],
    invariant_codes: list[str],
    action_type: str,
    harm_signals: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    passport_id = stable_id("dp", tenant_key, decision_class, subject_id, occurred_at)
    evidence_id = stable_id("ev", evidence["envelope_id"])
    anchor_id = stable_id("an", evidence["envelope_id"])
    now = occurred_at
    checks = [
        {
            "invariant_code": code,
            "bundle_hash": hashlib.sha256(f"{tenant_key}|{code}|1.0.0".encode()).hexdigest(),
            "result": "pass",
            "source_status": "primary_verified",
            "detail_ref": None,
        }
        for code in invariant_codes
    ]
    return {
        "schema_version": "1.0.0",
        "passport_id": passport_id,
        "tenant_id": tenant_key,
        "project_id": project_id,
        "decision_class": decision_class,
        "status": "reconciled",
        "subject_refs": [{"kind": subject_kind, "id": subject_id, "effective_at": occurred_at}],
        "event_window": {"occurred_start": occurred_at, "occurred_end": occurred_at, "business_dates": [occurred_at[:10]], "timezone_context": ["UTC"]},
        "evidence": [{"evidence_id": evidence_id, "envelope_id": evidence["envelope_id"], "source_system": evidence["source"]["system"], "kind": "manual_entry" if action_type == "correct" else "api_pull", "sha256": evidence["payload_sha256"], "anchor_candidate": True}],
        "anchors": [{"anchor_id": anchor_id, "anchor_type": "runtime_receipt", "integrity_score": 0.95, "independence_class": "semi_independent", "degradation_reason": None}],
        "anchor_integrity_avg": 0.95,
        "invariant_checks": checks,
        "writer": {"actor_type": "agent", "actor_id": "synthetic-generator", "model_or_role": "deterministic_writer"},
        "evaluator": {"actor_type": "service", "actor_id": "acceptance-validator", "model_or_role": "separate_evaluator"},
        "approval_chain": [{"step": "synthetic_acceptance", "approver": {"actor_type": "service", "actor_id": "acceptance-validator", "model_or_role": "validator"}, "decision": "approved", "decided_at": now, "dual_key_group": None}],
        "action": {"action_type": action_type, "requested_changes": ["record synthetic protected event"], "rollback_plan_ref": None},
        "observed_ukg_state": {"ukg_object_refs": [], "observed_at": now, "state_hash": evidence["payload_sha256"]},
        "payroll_publication": {"publication_state": "not_started", "outbox_key": hashlib.sha256(passport_id.encode()).hexdigest(), "bundle_hash": None},
        "reconciliation": {"status": "complete", "wage_protection_applied": bool(harm_signals), "delta_batch_refs": []},
        "worker_harm_signals": harm_signals or [],
        "assurance": {"passport_completeness": 100, "anchor_integrity_avg": 95, "assurance_score": 97, "cross_tenant_isolation_passed": True},
        "hash_chain": [{"kind": "evidence", "sha256": evidence["payload_sha256"]}],
    }
