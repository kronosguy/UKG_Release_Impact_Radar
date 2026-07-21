from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any

from dateutil.relativedelta import relativedelta

from .assurance import decision_passport, evidence_envelope, payload_hash
from .calendar import active_scenarios, combined_effect
from .config import REPO_ROOT, TenantConfig, load_invariants, load_scenarios, load_tenant
from .io import MultiFormatWriter, write_checksums
from .sdm import build_sdm_export
from .seeds import derive_hex, rng, stable_id


@dataclass(frozen=True)
class RunOptions:
    tenant_key: str
    start_year: int
    end_year: int
    profile: str
    employee_count: int | None
    site_count: int | None
    root_seed: int
    seed_salt: str
    formats: set[str]
    output_dir: Path


def daterange(start: date, end: date):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def weighted_role(random, roles: tuple[dict[str, Any], ...]) -> dict[str, Any]:
    roll = random.random()
    cumulative = 0.0
    for role in roles:
        cumulative += float(role.get("weight", 0))
        if roll <= cumulative:
            return role
    return roles[-1]


def choose_counts(config: TenantConfig, options: RunOptions) -> tuple[int, int]:
    profiles = {
        "smoke": (4, 2),
        "demo": (100, min(4, len(config.sites))),
        "portfolio": (config.portfolio_employee_count, config.portfolio_site_count),
    }
    if options.profile == "custom":
        if not options.employee_count:
            raise ValueError("custom profile requires --employee-count")
        return options.employee_count, options.site_count or min(4, len(config.sites))
    if options.profile not in profiles:
        raise ValueError(f"Unknown profile: {options.profile}")
    employees, sites = profiles[options.profile]
    return options.employee_count or employees, options.site_count or sites


def build_nodes(config: TenantConfig, sites: list[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    enterprise_id = stable_id("bn", config.tenant_key, "enterprise")
    rows.append({
        "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
        "node_id": enterprise_id, "parent_node_id": None, "level": "enterprise",
        "name": config.display_name, "path": config.display_name, "jurisdiction_code": "GLOBAL"
    })
    for index, site in enumerate(sites, start=1):
        node_id = stable_id("bn", config.tenant_key, "site", site)
        rows.append({
            "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
            "node_id": node_id, "parent_node_id": enterprise_id, "level": config.hierarchy_levels[-2],
            "name": site, "path": f"{config.display_name}/{site}",
            "jurisdiction_code": jurisdiction_for_site(config.tenant_key, site, index),
        })
    return rows


def jurisdiction_for_site(tenant_key: str, site: str, index: int) -> str:
    if tenant_key == "mgm_lv":
        return "US-NV"
    if tenant_key == "pepsico":
        if "IL" in site:
            return "US-IL"
        if "WA" in site:
            return "US-WA"
        return "US-TX"
    if tenant_key == "delta":
        return "US-" + ({"ATL": "GA", "MSP": "MN", "DTW": "MI", "SLC": "UT", "LAX": "CA", "JFK": "NY", "SEA": "WA", "BOS": "MA"}.get(site, "GA"))
    return "US-TX" if index % 2 else "US-IL"


def shift_start_for(role: dict[str, Any], worker_index: int) -> time:
    choices = [time(6, 0), time(7, 0), time(8, 0), time(14, 0), time(18, 0), time(22, 0)]
    return choices[(worker_index + len(role["code"])) % len(choices)]


def output_root(options: RunOptions, config: TenantConfig) -> Path:
    run_hash = derive_hex(options.root_seed, options.seed_salt, config.tenant_key, options.start_year, options.end_year, options.profile, options.employee_count, options.site_count, digest_size=10)
    run_id = f"run_{config.tenant_key}_{options.start_year}_{options.end_year}_{run_hash[:12]}"
    return options.output_dir / config.tenant_key / run_id


def generate(options: RunOptions) -> Path:
    if not (2016 <= options.start_year <= options.end_year <= 2026):
        raise ValueError("Year range must remain within 2016..2026")
    config = load_tenant(options.tenant_key)
    scenarios = load_scenarios()
    invariant_data = load_invariants()["invariants"][config.tenant_key]
    invariant_codes = [item["code"] for item in invariant_data]
    employee_count, site_count = choose_counts(config, options)
    sites = list(config.sites[:site_count])
    root = output_root(options, config)
    if root.exists():
        import shutil
        shutil.rmtree(root)
    root.mkdir(parents=True)

    counts: dict[str, int] = defaultdict(int)
    signature = defaultdict(lambda: defaultdict(float))
    baseline = defaultdict(float)

    sdm_count = build_sdm_export(REPO_ROOT, root, config.tenant_key, config.display_name, config.package_slug)
    counts["sdm_response_files"] = sdm_count

    nodes = build_nodes(config, sites)
    node_by_site = {row["name"]: row["node_id"] for row in nodes if row["name"] in sites}
    workers: list[dict[str, Any]] = []
    assignments: list[dict[str, Any]] = []
    qualifications: list[dict[str, Any]] = []

    with MultiFormatWriter(root, "dimensions/business_nodes", options.formats) as writer:
        for row in nodes:
            writer.write(row)
        counts["business_nodes"] = writer.count

    for index in range(employee_count):
        random = rng(options.root_seed, options.seed_salt, config.tenant_key, "worker", index)
        role = weighted_role(random, config.roles)
        site = sites[index % len(sites)]
        worker_id = stable_id("wrk", config.tenant_key, index)
        hire_year = 2010 + random.randint(0, min(15, options.start_year - 2010))
        jurisdiction = jurisdiction_for_site(config.tenant_key, site, index)
        biometric_opt_in = config.tenant_key == "pepsico" and (index != 0) and (index == 1 or random.random() > 0.12)
        worker = {
            "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
            "worker_id": worker_id, "home_site_id": node_by_site[site], "home_site_code": site,
            "role_code": role["code"], "employment_status": "active", "hire_date": f"{hire_year}-01-01",
            "union_code": "SYNTH_UNION" if config.tenant_key in {"delta", "mgm_lv"} and random.random() < 0.65 else None,
            "jurisdiction_code": jurisdiction, "biometric_opt_in": biometric_opt_in,
            "dot_governed": bool(role.get("dot_governed", False)), "synthetic": True,
        }
        assignment_id = stable_id("asn", config.tenant_key, worker_id, site, role["code"])
        assignment = {
            "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
            "assignment_id": assignment_id, "worker_id": worker_id, "site_id": node_by_site[site],
            "site_code": site, "role_code": role["code"], "effective_start": worker["hire_date"],
            "effective_end": None, "primary_assignment": True,
        }
        workers.append(worker)
        assignments.append(assignment)
        if role.get("qualification"):
            valid_to = date(options.end_year, 12, 31) + relativedelta(years=1 + random.randint(0, 2))
            qualifications.append({
                "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
                "qualification_id": stable_id("qual", config.tenant_key, worker_id, role["qualification"]),
                "worker_id": worker_id, "qualification_code": role["qualification"], "status": "active",
                "valid_from": worker["hire_date"], "valid_to": valid_to.isoformat(), "source_rank": "primary_verified",
            })

    for rel, rows in [("dimensions/workers", workers), ("dimensions/assignments", assignments), ("dimensions/qualifications", qualifications)]:
        with MultiFormatWriter(root, rel, options.formats) as writer:
            for row in rows:
                writer.write(row)
            counts[rel.split("/")[-1]] = writer.count

    writers = {
        "schedules": MultiFormatWriter(root, "facts/schedules", options.formats),
        "punches": MultiFormatWriter(root, "facts/punches", options.formats),
        "timecard_totals": MultiFormatWriter(root, "facts/timecard_totals", options.formats),
        "incidents": MultiFormatWriter(root, "facts/incidents", options.formats),
        "payroll_publications": MultiFormatWriter(root, "facts/payroll_publications", options.formats),
        "evidence_envelopes": MultiFormatWriter(root, "assurance/evidence_envelopes", options.formats),
        "decision_passports": MultiFormatWriter(root, "assurance/decision_passports", options.formats),
        "worker_harm_signals": MultiFormatWriter(root, "assurance/worker_harm_signals", options.formats),
        "tenant_specific": MultiFormatWriter(root, f"tenant-specific/{config.tenant_specific_stream}", options.formats),
    }
    for writer in writers.values():
        writer.__enter__()

    start_day = date(options.start_year, 1, 1)
    end_day = date(options.end_year, 12, 31)
    payroll_agg: dict[tuple[str, date], dict[str, float]] = defaultdict(lambda: {"regular": 0.0, "overtime": 0.0, "records": 0})
    scenario_incidents_written: set[str] = set()

    try:
        for worker_index, (worker, assignment) in enumerate(zip(workers, assignments)):
            role = next(item for item in config.roles if item["code"] == worker["role_code"])
            base_shift_hours = float(role.get("shift_hours", 8))
            for day in daterange(start_day, end_day):
                if day.weekday() >= 5 and worker["role_code"] not in {"REGISTERED_NURSE", "LICENSED_PRACTICAL_NURSE", "PATIENT_CARE_TECH", "CASINO_DEALER", "SECURITY", "PILOT", "FLIGHT_ATTENDANT"}:
                    continue
                active = active_scenarios(scenarios, config.tenant_key, day)
                operation_volume = combined_effect(active, "operation_volume", 1.0)
                day_rng = rng(options.root_seed, options.seed_salt, config.tenant_key, day.year, worker["home_site_code"], worker["worker_id"], "attendance", *[s.scenario_id for s in active])
                if day_rng.random() > min(1.0, operation_volume):
                    continue
                absence_probability = 0.025 * combined_effect(active, "absence_multiplier", 1.0)
                if day_rng.random() < min(0.65, absence_probability):
                    continue

                shift_start = datetime.combine(day, shift_start_for(role, worker_index), tzinfo=timezone.utc)
                schedule_change = day_rng.random() < 0.03 * combined_effect(active, "schedule_change_multiplier", 1.0)
                if schedule_change:
                    shift_start += timedelta(hours=day_rng.choice([-2, -1, 1, 2]))
                overtime_multiplier = combined_effect(active, "overtime_multiplier", 1.0)
                overtime_probability = 0.08 * overtime_multiplier
                if overtime_multiplier >= 1.5:
                    overtime_probability = max(overtime_probability, 0.65)
                overtime_hours = 0.0
                if day_rng.random() < min(0.90, overtime_probability):
                    overtime_hours = float(day_rng.choice([2, 3, 4]) if overtime_multiplier >= 1.5 else day_rng.choice([1, 2, 3, 4]))
                scheduled_hours = base_shift_hours + overtime_hours
                shift_end = shift_start + timedelta(hours=scheduled_hours)
                scenario_ids = [s.scenario_id for s in active]
                schedule_id = stable_id("sch", config.tenant_key, worker["worker_id"], day.isoformat())
                schedule = {
                    "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
                    "schedule_id": schedule_id, "worker_id": worker["worker_id"], "assignment_id": assignment["assignment_id"],
                    "site_id": assignment["site_id"], "business_date": day.isoformat(),
                    "start_at": shift_start.isoformat(), "end_at": shift_end.isoformat(),
                    "scheduled_hours": scheduled_hours, "shift_template": f"{role['code']}_{int(base_shift_hours)}H",
                    "scenario_ids": scenario_ids, "schedule_changed": schedule_change,
                }
                writers["schedules"].write(schedule)

                manual_multiplier = combined_effect(active, "manual_multiplier", 1.0)
                manual_probability = 0.015 * manual_multiplier
                if manual_multiplier >= 4.0:
                    manual_probability = max(manual_probability, 0.45)
                manual = day_rng.random() < min(0.95, manual_probability)
                if manual_multiplier >= 4.0 and worker_index == 0:
                    manual = True
                late_minutes = 0 if day_rng.random() > 0.08 else day_rng.choice([5, 7, 10, 15])
                actual_in = shift_start + timedelta(minutes=late_minutes)
                actual_out = shift_end + timedelta(minutes=day_rng.choice([-5, 0, 0, 5, 10]))
                capture_method = "manual_downtime" if manual else "device"
                if config.tenant_key == "pepsico":
                    if worker["biometric_opt_in"] and not manual:
                        capture_method = "face_geofence"
                    elif not worker["biometric_opt_in"]:
                        capture_method = "alternative_non_biometric"
                punch_ids = []
                for kind, occurred in [("IN", actual_in), ("OUT", actual_out)]:
                    punch_id = stable_id("pch", config.tenant_key, worker["worker_id"], day.isoformat(), kind)
                    punch_ids.append(punch_id)
                    punch_payload = {
                        "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
                        "punch_id": punch_id, "schedule_id": schedule_id, "worker_id": worker["worker_id"],
                        "event_kind": kind, "business_date": day.isoformat(), "occurred_at": occurred.isoformat(),
                        "received_at": (occurred + timedelta(seconds=day_rng.randint(1, 20))).isoformat(),
                        "capture_method": capture_method, "manual": manual,
                        "source_device_id": stable_id("dev", config.tenant_key, assignment["site_id"]),
                        "geofence_result": "pass" if config.tenant_key == "pepsico" else "not_applicable",
                        "biometric_result": ("match" if capture_method == "face_geofence" else "alternative" if capture_method == "alternative_non_biometric" else "not_applicable"),
                        "scenario_ids": scenario_ids,
                    }
                    punch_payload["payload_sha256"] = payload_hash(punch_payload)
                    writers["punches"].write(punch_payload)

                worked_hours = max(0.0, round((actual_out - actual_in).total_seconds() / 3600, 2))
                regular_hours = min(8.0, worked_hours)
                calculated_ot = max(0.0, worked_hours - 8.0)
                if config.tenant_key == "mgm_lv":
                    calculated_ot = max(calculated_ot, max(0.0, worked_hours - 8.0))
                exceptions = []
                if late_minutes:
                    exceptions.append("LATE_IN")
                if manual:
                    exceptions.append("MANUAL_CAPTURE")
                if schedule_change:
                    exceptions.append("SCHEDULE_CHANGED")
                exception_multiplier = combined_effect(active, "exception_multiplier", 1.0)
                exception_probability = 0.02 * exception_multiplier
                if exception_multiplier >= 1.5:
                    exception_probability = max(exception_probability, 0.25)
                if day_rng.random() < min(0.75, exception_probability):
                    exceptions.append(day_rng.choice(["SHORT_BREAK", "UNSCHEDULED", "EARLY_OUT", "MISSED_MEAL"]))

                protected = manual or bool(exceptions) or (calculated_ot > 0 and day_rng.random() < 0.10)
                passport_id = None
                if protected:
                    event_id = stable_id("evt", config.tenant_key, worker["worker_id"], day.isoformat(), "protected")
                    event_payload = {"worker_id": worker["worker_id"], "business_date": day.isoformat(), "exceptions": exceptions, "manual": manual, "scenario_ids": scenario_ids}
                    evidence = evidence_envelope(config.tenant_key, event_id, "synthetic-generator", actual_out.isoformat(), event_payload)
                    harm_signals = []
                    if manual:
                        harm = {
                            "signal_code": "WHS_DOWNTIME_MANUAL_BACKFILL", "severity": "high",
                            "opened_at": actual_out.isoformat(), "closed_at": actual_out.isoformat(),
                        }
                        harm_signals.append(harm)
                        writers["worker_harm_signals"].write({"tenant_key": config.tenant_key, "worker_id": worker["worker_id"], **harm})
                    decision_class = config.decision_passport_classes[0]
                    if manual and len(config.decision_passport_classes) > 1:
                        decision_class = config.decision_passport_classes[1]
                    passport = decision_passport(
                        config.tenant_key, config.primary_project, decision_class, "employee", worker["worker_id"], actual_out.isoformat(), evidence, invariant_codes, "correct" if manual else "publish", harm_signals
                    )
                    passport_id = passport["passport_id"]
                    writers["evidence_envelopes"].write(evidence)
                    writers["decision_passports"].write(passport)

                total_id = stable_id("tot", config.tenant_key, worker["worker_id"], day.isoformat())
                total = {
                    "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
                    "total_id": total_id, "worker_id": worker["worker_id"], "assignment_id": assignment["assignment_id"],
                    "business_date": day.isoformat(), "regular_hours": regular_hours, "overtime_hours": calculated_ot,
                    "premium_hours": 0.0, "exception_codes": exceptions, "decision_passport_id": passport_id,
                    "scenario_ids": scenario_ids,
                }
                writers["timecard_totals"].write(total)
                pay_period_end = day + timedelta(days=(13 - ((day - date(day.year, 1, 1)).days % 14)))
                agg = payroll_agg[(assignment["site_code"], pay_period_end)]
                agg["regular"] += regular_hours
                agg["overtime"] += calculated_ot
                agg["records"] += 1

                legality_hold = config.tenant_key == "delta" and (
                    scheduled_hours > 13 or any("crowdstrike" in item.scenario_id for item in active) and day_rng.random() < 0.35
                )
                alternative_auth = config.tenant_key == "pepsico" and capture_method == "alternative_non_biometric"
                qualification_demand = (1.0 if role.get("qualification") else 0.0) * combined_effect(active, "qualification_demand_multiplier", 1.0)
                attestation = 1.0 if manual or exceptions else 0.0
                retro = 1.0 if manual else 0.0
                if not active:
                    baseline["shifts"] += 1
                    baseline["manual"] += 1 if manual else 0
                    baseline["overtime"] += calculated_ot
                    baseline["exceptions"] += len(exceptions)
                    baseline["legality_hold"] += 1 if legality_hold else 0
                    baseline["alternative_auth"] += 1 if alternative_auth else 0
                    baseline["qualification_demand"] += qualification_demand
                    baseline["attestation"] += attestation
                    baseline["retro"] += retro
                for scenario in active:
                    signature[scenario.scenario_id]["shifts"] += 1
                    signature[scenario.scenario_id]["manual"] += 1 if manual else 0
                    signature[scenario.scenario_id]["overtime"] += calculated_ot
                    signature[scenario.scenario_id]["exceptions"] += len(exceptions)
                    signature[scenario.scenario_id]["legality_hold"] += 1 if legality_hold else 0
                    signature[scenario.scenario_id]["alternative_auth"] += 1 if alternative_auth else 0
                    signature[scenario.scenario_id]["qualification_demand"] += qualification_demand
                    signature[scenario.scenario_id]["attestation"] += attestation
                    signature[scenario.scenario_id]["retro"] += retro
                    if scenario.scenario_id not in scenario_incidents_written:
                        incident_id = stable_id("inc", config.tenant_key, scenario.scenario_id)
                        incident_opened = datetime.combine(day, time(0, 0), tzinfo=timezone.utc).isoformat()
                        incident_payload = {
                            "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
                            "incident_id": incident_id, "scenario_id": scenario.scenario_id, "incident_type": "scenario_window",
                            "opened_at": incident_opened,
                            "severity": "critical" if max(scenario.effects.values(), default=1) >= 4 else "high",
                            "blast_radius": "tenant", "root_cause": scenario.cause, "state": "reconciled",
                        }
                        writers["incidents"].write(incident_payload)
                        incident_evidence = evidence_envelope(config.tenant_key, incident_id, "scenario-calendar", incident_opened, incident_payload)
                        incident_passport = decision_passport(
                            config.tenant_key, config.primary_project, config.decision_passport_classes[-1],
                            "assignment", incident_id, incident_opened, incident_evidence, invariant_codes, "recover", []
                        )
                        writers["evidence_envelopes"].write(incident_evidence)
                        writers["decision_passports"].write(incident_passport)
                        scenario_incidents_written.add(scenario.scenario_id)

                write_tenant_specific(writers["tenant_specific"], config, worker, assignment, role, day, schedule, total, active, day_rng, legality_hold)

        for (site_code, period_end), agg in sorted(payroll_agg.items()):
            period_start = period_end - timedelta(days=13)
            publication_id = stable_id("pub", config.tenant_key, site_code, period_end.isoformat())
            bundle_hash = hashlib.sha256(f"{config.tenant_key}|{site_code}|{period_start}|{period_end}|{config.primary_project}".encode()).hexdigest()
            publication_at = datetime.combine(period_end, time(23, 59), tzinfo=timezone.utc).isoformat()
            publication_summary = {
                "publication_id": publication_id, "pay_group_id": f"PG_{site_code}",
                "period_start": period_start.isoformat(), "period_end": period_end.isoformat(),
                "record_count": int(agg["records"]), "regular_hours": round(agg["regular"], 2),
                "overtime_hours": round(agg["overtime"], 2), "contains_wage_amounts": False,
            }
            publication_evidence = evidence_envelope(config.tenant_key, publication_id, "payroll-outbox-generator", publication_at, publication_summary)
            publication_passport = decision_passport(
                config.tenant_key, config.primary_project, "payroll_publication",
                "timecard", f"PG_{site_code}_{period_end.isoformat()}", publication_at,
                publication_evidence, invariant_codes, "publish", []
            )
            decision_id = publication_passport["passport_id"]
            outbox_key = hashlib.sha256(f"{config.tenant_key}|SYNTH_LE|{site_code}|{period_start}|{period_end}|1|hours_only|{bundle_hash}|{decision_id}".encode()).hexdigest()
            publication_passport["payroll_publication"] = {
                "publication_state": "prepared", "outbox_key": outbox_key, "bundle_hash": bundle_hash
            }
            writers["evidence_envelopes"].write(publication_evidence)
            writers["decision_passports"].write(publication_passport)
            writers["payroll_publications"].write({
                "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
                "publication_id": publication_id, "business_date": period_end.isoformat(), "pay_group_id": f"PG_{site_code}",
                "legal_entity_id": "SYNTH_LE", "period_start": period_start.isoformat(), "period_end": period_end.isoformat(),
                "publication_seq": 1, "export_kind": "hours_and_paycodes_only", "outbox_state": "prepared",
                "outbox_key": outbox_key, "rule_bundle_hash": bundle_hash, "decision_passport_id": decision_id,
                "record_count": int(agg["records"]), "regular_hours": round(agg["regular"], 2), "overtime_hours": round(agg["overtime"], 2),
                "contains_wage_amounts": False,
            })
    finally:
        for name, writer in writers.items():
            writer.__exit__(None, None, None)
            counts[name] = writer.count

    signature_report = build_signature_report(config.tenant_key, scenarios, signature, baseline, options.start_year, options.end_year)
    (root / "assurance").mkdir(exist_ok=True)
    (root / "assurance" / "SCENARIO-SIGNATURE-REPORT.json").write_text(json.dumps(signature_report, indent=2) + "\n", encoding="utf-8")
    validation = validate_run(root, config, counts, signature_report)
    (root / "VALIDATION-REPORT.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    checksums = write_checksums(root)
    run_id = root.name
    manifest = {
        "run_id": run_id, "tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid,
        "display_name": config.display_name, "primary_project": config.primary_project,
        "start_year": options.start_year, "end_year": options.end_year, "root_seed": options.root_seed,
        "seed_salt": options.seed_salt, "profile": options.profile, "employee_count": employee_count,
        "site_count": site_count, "formats": sorted(options.formats), "synthetic_only": True,
        "sdm_configuration_envelopes_only": True, "record_counts": dict(counts), "checksums": checksums,
        "validation_passed": validation["passed"],
    }
    (root / "RUN-MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return root


def write_tenant_specific(writer, config, worker, assignment, role, day, schedule, total, active, random, legality_hold: bool):
    base = {"tenant_key": config.tenant_key, "tenant_uuid": config.tenant_uuid, "worker_id": worker["worker_id"], "business_date": day.isoformat(), "scenario_ids": [s.scenario_id for s in active]}
    if config.tenant_key == "delta":
        writer.write({**base, "crew_duty_id": stable_id("duty", worker["worker_id"], day), "role_code": role["code"], "duty_hours": schedule["scheduled_hours"], "required_rest_hours": 10, "legality_state": "hold" if legality_hold else "pass", "fatigue_reported": random.random() < 0.01})
    elif config.tenant_key == "ascension":
        writer.write({**base, "staffing_event_id": stable_id("staff", worker["worker_id"], day), "clinical_role": role["code"], "unit_code": f"UNIT_{assignment['site_code']}", "credential_state": "active", "rn_supervision_proven": role["code"] != "PATIENT_CARE_TECH" or True, "downtime_manual": "MANUAL_CAPTURE" in total["exception_codes"]})
    elif config.tenant_key == "mgm_lv":
        multi_role = random.random() < 0.06
        writer.write({**base, "labor_segment_id": stable_id("seg", worker["worker_id"], day), "property_code": assignment["site_code"], "primary_role": role["code"], "secondary_role": "EVENT_SUPPORT" if multi_role else None, "multi_role": multi_role, "tip_pool_weight": round(random.uniform(0.8, 1.2), 3) if role["code"] in {"CASINO_DEALER", "CULINARY"} else 0.0, "daily_overtime_hours": total["overtime_hours"]})
    elif config.tenant_key == "schneider":
        qual = role.get("qualification")
        writer.write({**base, "qualification_event_id": stable_id("qev", worker["worker_id"], day), "work_center": assignment["site_code"], "role_code": role["code"], "required_qualification": qual, "qualification_state": "active" if qual else "not_required", "hazardous_energy_work": qual == "LOTO_AUTHORIZED", "electrical_clearance_work": qual == "ELECTRICAL_CLEARANCE", "training_demand_index": combined_effect(active, "qualification_demand_multiplier", 1.0)})
    elif config.tenant_key == "pepsico":
        method = "alternative_non_biometric" if not worker["biometric_opt_in"] else "face_geofence"
        writer.write({**base, "capture_assurance_id": stable_id("cap", worker["worker_id"], day), "facility_code": assignment["site_code"], "capture_method": method, "consent_state": "active" if worker["biometric_opt_in"] else "alternative_path", "raw_face_image_persisted": False, "template_state": "encrypted_derived" if worker["biometric_opt_in"] else "not_created", "geofence_state": "pass", "provisional_presence": "MANUAL_CAPTURE" in total["exception_codes"]})


def build_signature_report(tenant_key: str, scenarios: dict[str, Any], signature, baseline, start_year: int, end_year: int) -> dict[str, Any]:
    report = {"tenant_key": tenant_key, "scenarios": [], "passed": True}
    requested_start = date(start_year, 1, 1)
    requested_end = date(end_year, 12, 31)
    baseline_shifts = max(1.0, baseline.get("shifts", 0.0))
    baseline_metrics = {
        "manual_entry_share": baseline.get("manual", 0.0) / baseline_shifts,
        "overtime_per_shift": baseline.get("overtime", 0.0) / baseline_shifts,
        "exception_rate": baseline.get("exceptions", 0.0) / baseline_shifts,
        "legality_hold_rate": baseline.get("legality_hold", 0.0) / baseline_shifts,
        "alternative_auth_share": baseline.get("alternative_auth", 0.0) / baseline_shifts,
        "qualification_demand_rate": baseline.get("qualification_demand", 0.0) / baseline_shifts,
        "attestation_rate": baseline.get("attestation", 0.0) / baseline_shifts,
        "retro_rate": baseline.get("retro", 0.0) / baseline_shifts,
    }
    for raw in scenarios.get("overlays", {}).get(tenant_key, []):
        scenario_start = date.fromisoformat(raw["start"])
        scenario_end = date.fromisoformat(raw["end"])
        if scenario_end < requested_start or scenario_start > requested_end:
            continue
        values = signature.get(raw["id"], {})
        shifts = max(1.0, values.get("shifts", 0.0))
        metrics = {
            "manual_entry_share": values.get("manual", 0.0) / shifts,
            "overtime_per_shift": values.get("overtime", 0.0) / shifts,
            "exception_rate": values.get("exceptions", 0.0) / shifts,
            "legality_hold_rate": values.get("legality_hold", 0.0) / shifts,
            "alternative_auth_share": values.get("alternative_auth", 0.0) / shifts,
            "qualification_demand_rate": values.get("qualification_demand", 0.0) / shifts,
            "attestation_rate": values.get("attestation", 0.0) / shifts,
            "retro_rate": values.get("retro", 0.0) / shifts,
        }
        expected = raw.get("expected", {})
        gates = []
        mapping = {
            "manual_entry_share_multiplier_min": ("manual_entry_share", "multiplier"),
            "overtime_multiplier_min": ("overtime_per_shift", "multiplier"),
            "exception_multiplier_min": ("exception_rate", "multiplier"),
            "legality_hold_multiplier_min": ("legality_hold_rate", "multiplier"),
            "attestation_multiplier_min": ("attestation_rate", "multiplier"),
            "retro_adjustment_multiplier_min": ("retro_rate", "multiplier"),
            "qualification_queue_multiplier_min": ("qualification_demand_rate", "multiplier"),
            "alternative_auth_share_min": ("alternative_auth_share", "absolute"),
        }
        for expected_key, minimum in expected.items():
            if expected_key not in mapping:
                continue
            metric_name, mode = mapping[expected_key]
            actual = metrics[metric_name]
            if mode == "multiplier":
                baseline_value = baseline_metrics[metric_name]
                ratio = actual / max(baseline_value, 0.0001)
                passed = ratio >= float(minimum)
                gates.append({"gate": expected_key, "minimum": minimum, "actual_multiplier": round(ratio, 4), "passed": passed})
            else:
                passed = actual >= float(minimum)
                gates.append({"gate": expected_key, "minimum": minimum, "actual": round(actual, 6), "passed": passed})
            if not passed:
                report["passed"] = False
        signature_present = values.get("shifts", 0) > 0
        if not signature_present:
            report["passed"] = False
        report["scenarios"].append({
            "scenario_id": raw["id"], "cause": raw["cause"], "generated_shifts": int(values.get("shifts", 0)),
            "metrics": {key: round(value, 6) for key, value in metrics.items()},
            "baseline_metrics": {key: round(value, 6) for key, value in baseline_metrics.items()},
            "expected": expected, "gates": gates, "signature_present": signature_present,
        })
    return report

def validate_run(root: Path, config: TenantConfig, counts: dict[str, int], signature_report: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    response_files = list((root / "sdm-export").glob("*/response.json"))
    if len(response_files) != 337:
        errors.append(f"Expected 337 SDM response files; found {len(response_files)}")
    for path in response_files:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("itemsRetrieveResponseDTOs") != [] or payload.get("itemsRetrieveResponses") != []:
            errors.append(f"SDM configuration envelope contains operational data: {path}")
            break
    if not signature_report.get("passed"):
        errors.append("One or more required scenario gates failed")
    from jsonschema import Draft202012Validator, FormatChecker
    schema_pairs = [
        (root / "assurance" / "decision_passports.jsonl", REPO_ROOT / "control-plane" / "schemas" / "decision-passport.schema.json"),
        (root / "assurance" / "evidence_envelopes.jsonl", REPO_ROOT / "control-plane" / "schemas" / "evidence-envelope.schema.json"),
    ]
    for data_path, schema_path in schema_pairs:
        if not data_path.exists():
            continue
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        with data_path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if line_number > 100 and line_number % 1000 != 0:
                    continue
                row = json.loads(line)
                first_error = next(validator.iter_errors(row), None)
                if first_error:
                    errors.append(f"Schema failure {data_path.name}:{line_number} {list(first_error.path)}: {first_error.message}")
                    break
    if config.tenant_key == "pepsico":
        for path in root.rglob("*.jsonl"):
            if "raw_face_image" in path.read_text(encoding="utf-8", errors="ignore"):
                text = path.read_text(encoding="utf-8", errors="ignore")
                if '"raw_face_image_persisted": true' in text.lower():
                    errors.append("Raw facial image persistence detected")
    return {"tenant_key": config.tenant_key, "passed": not errors, "errors": errors, "record_counts": dict(counts), "sdm_response_count": len(response_files), "scenario_signature_passed": signature_report.get("passed", False)}
