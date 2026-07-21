# UKG_WORKFORCE_ASSURANCE_CONSTITUTION_FINAL.md

## Determination and tenant model

**Executive determination**

The platform category is **Workforce Decision Assurance**, not generic workflow automation and not generic workforce analytics. Its atomic trust unit is the **Decision Passport**. Its deployment model is **five isolated tenant overlays on one shared assurance control plane**: Delta Air Lines on P03, Ascension Healthcare on P02, MGM Resorts Las Vegas on P01, Schneider Electric on P04, and PepsiCo on P05. The non-negotiable proof chain is:

**real-world event → trusted capture → effective-dated context → policy-bound interpretation → immutable temporal evidence → causal analysis → guarded action → observed UKG state → payroll publication → worker-safe reconciliation → architecture learning**

That proof chain is the direct operational answer to the transcript corpus’ core warning: systems go structurally blind when they optimize proxies, let measurement decay behind green dashboards, or validate claims only against other claims rather than against anchors that the system itself cannot fabricate. The same corpus requires anchors and anchor-integrity scoring, a frozen set that optimizers cannot weaken, human origination of the root value hierarchy, mediation around the model rather than model worship, comparative measurement of workflow variants, containment rather than command, and pain channels that bypass bureaucracy when safety or pay is on the line. fileciteturn0file0L31-L40 fileciteturn0file0L63-L117 fileciteturn0file0L531-L544 fileciteturn0file0L549-L556 fileciteturn0file0L593-L606 fileciteturn0file0L614-L623 fileciteturn0file0L1426-L1445 fileciteturn0file0L1518-L1531 fileciteturn0file0L2741-L2747 fileciteturn0file0L7735-L7742 fileciteturn0file0L8061-L8076

This constitution also constrains the UKG integration surface to what UKG publicly documents today. UKG Webhooks provides near-real-time event delivery with HMAC support; Webhooks Premium adds retry, audit, replay, and retrieval by event ID; the Developer Console is role-based and manages machine-to-machine credentials; Workforce Intelligence Hub is still an MVP for a limited U.S. customer set; and People Fabric is described publicly only at a high level as suite-wide data. So the platform uses Webhooks and Premium replay for operational truth, uses Developer Console credential boundaries for integration control, and treats People Fabric as **enrichment-only** until workload-specific reliability is proven by tenant certification. citeturn2search4turn2search2turn2search11turn2search3turn2search0turn3search0

**Source discipline table**

Every source below is either `primary_verified` and allowed into frozen invariants, or `design_heuristic` and therefore barred from payroll-, legality-, safety-, or isolation-impacting automation unless later replaced by a primary source.

| source_id | status | publisher | primary_url | citation | effective_or_updated | access_date | constitutional use | proof |
|---|---|---|---|---|---|---|---|---|
| `faa_part_117` | `primary_verified` | FAA / eCFR | `https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-117` | 14 C.F.R. Part 117 | current through 2026-07-07 | 2026-07-21 | Delta flight/duty/rest limits and FRMS spine | citeturn23search8turn23search4 |
| `faa_ac_117_2` | `primary_verified` | FAA | `https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentid/1020388` | AC 117-2 Fatigue Education and Awareness Training Program | 2012-10-11 | 2026-07-21 | Delta fatigue education and reporting | citeturn23search2 |
| `fmcsa_hos_summary` | `primary_verified` | FMCSA | `https://www.fmcsa.dot.gov/regulations/hours-service/summary-hours-service-regulations` | FMCSA Hours of Service summary | current page | 2026-07-21 | DOT/HOS packs for PepsiCo transport-adjacent flows and any Schneider fleet-adjacent field operations | citeturn22search2 |
| `cms_482_23` | `primary_verified` | CMS / eCFR | `https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-482/subpart-C/section-482.23` | 42 C.F.R. § 482.23 Nursing services | current through 2026-07-01 | 2026-07-21 | Ascension staffing, licensure validity, RN supervision, 24-hour coverage | citeturn24search0 |
| `nlc_compact` | `primary_verified` | NCSBN / NLC Commission | `https://www.ncsbn.org/compacts` | Nurse Licensure Compact materials | current site state | 2026-07-21 | Ascension multistate mobility and compact-aware credential logic | citeturn13search3turn13search0 |
| `flsa_hours_worked` | `primary_verified` | U.S. Department of Labor | `https://www.dol.gov/agencies/whd/flsa/off-the-clock` | FLSA hours worked/off-the-clock guidance | current page | 2026-07-21 | Punch/pay evidence, off-the-clock protections, reconciliation thresholds | citeturn12search0turn12search1turn12search6 |
| `flsa_healthcare_hours` | `primary_verified` | U.S. Department of Labor | `https://www.dol.gov/agencies/whd/fact-sheets/53-healthcare-hours-worked` | Fact Sheet 53 Health Care Industry and Hours Worked | current page | 2026-07-21 | Ascension rounding, meal-break, and compensable-time tests | citeturn12search9 |
| `nevada_overtime` | `primary_verified` | Nevada Legislature / Labor Commissioner | `https://www.leg.state.nv.us/nrs/NRS-608.html#NRS608Sec018` | NRS 608.018 Overtime | current through 2026 legislative site | 2026-07-21 | MGM daily overtime, weekly overtime, 4x10 exception logic | citeturn14search7turn14search1 |
| `nevada_tips` | `primary_verified` | Nevada Legislature | `https://www.leg.state.nv.us/nrs/NRS-608.html#NRS608Sec160` | NRS 608.160 Tips and gratuities | current through 2026 legislative site | 2026-07-21 | MGM tip ownership and no-tip-credit invariants | citeturn14search5 |
| `osha_1910_147` | `primary_verified` | OSHA | `https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147` | 29 C.F.R. § 1910.147 Lockout/Tagout | current page | 2026-07-21 | Schneider hazardous-energy work authorization and maintenance quals | citeturn22search0 |
| `osha_1910_269` | `primary_verified` | OSHA | `https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.269` | 29 C.F.R. § 1910.269 Electric power generation, transmission, and distribution | current page | 2026-07-21 | Schneider electrical qualification, clearance, switching, and line-work controls | citeturn22search6 |
| `illinois_bipa` | `primary_verified` | Illinois General Assembly | `https://www.ilga.gov/ftp/ILCS/Ch%200740/Act%200014/074000140K15.html` | 740 ILCS 14 Sections 10 and 15 | original act 2008-10-03; amendments through P.A. 103-0769 | 2026-07-21 | PepsiCo biometric notice, consent, retention and destruction rules | citeturn15search6turn15search7turn15search8 |
| `texas_biometric_503_001` | `primary_verified` | Texas Legislature | `https://statutes.capitol.texas.gov/Docs/BC/htm/BC.503.htm#503.001` | Tex. Bus. & Com. Code § 503.001 | act eff. 2009-04-01; amended through 2025 session site | 2026-07-21 | PepsiCo biometric consent, storage, disclosure, destruction rules in Texas | citeturn18search0turn21search1 |
| `washington_biometrics_19_375` | `primary_verified` | Washington Legislature | `https://app.leg.wa.gov/RCW/default.aspx?cite=19.375&full=true` | Chapter 19.375 RCW Biometric identifiers | effective 2017-07-23 | 2026-07-21 | PepsiCo/WA biometric enrollment, retention, and disclosure logic | citeturn17search6 |
| `gdpr_article_9` | `primary_verified` | EUR-Lex | `https://eur-lex.europa.eu/eli/reg/2016/679/2016-05-04/eng` | Regulation (EU) 2016/679 Article 9 | 2016-05-04 text; applied 2018-05-25 | 2026-07-21 | PepsiCo and Schneider non-U.S. biometric and health-data restrictions | citeturn16search1 |
| `ico_worker_biometrics` | `primary_verified` | ICO | `https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/can-we-use-biometric-data-for-time-and-access-control-and-monitoring/` | ICO worker biometrics guidance | updated 2024-06-06 | 2026-07-21 | PepsiCo/Schneider UK worker alternatives, DPIA, manual review, no detriment | citeturn16search0turn16search2 |
| `ukg_webhooks` | `primary_verified` | UKG Developer Hub | `https://developer.ukg.com/proplatform/docs/welcome-to-ukg-webhooks` | UKG Webhooks docs | updated ~2026-05 | 2026-07-21 | Inbound real-time eventing, HMAC, test/deactivate/reactivate | citeturn2search4 |
| `ukg_webhooks_premium` | `primary_verified` | UKG Developer Hub | `https://developer.ukg.com/proplatform/docs/webhooks-premium` | Webhooks Premium docs | updated ~2026-05 | 2026-07-21 | Replay, retry, audit, high-volume contract | citeturn2search2turn2search1turn2search11 |
| `ukg_dev_console` | `primary_verified` | UKG Developer Hub | `https://developer.ukg.com/proplatform/docs/developer-console-quick-start` | Developer Console Quick Start | updated ~2026-05 | 2026-07-21 | Machine-to-machine credentials, RBAC-aligned issuance and revocation | citeturn2search3 |
| `ukg_wih` | `primary_verified` | UKG Developer Hub | `https://developer.ukg.com/proplatform/docs/welcome-to-workforce-intelligence-hub` | Workforce Intelligence Hub docs | updated ~2026-05 | 2026-07-21 | Monitor-only observability reference, not source of record | citeturn2search0 |
| `ukg_people_fabric` | `primary_verified` | UKG Developer Hub | `https://developer.ukg.com/flex/reference` | UKG Developer Hub landing page | current site | 2026-07-21 | Shows People Fabric as suite-wide data; constitution therefore constrains it to enrichment-only absent deeper guarantees | citeturn3search0 |
| `delta_crowdstrike_window` | `primary_verified` | Delta News Hub | `https://news.delta.com/update/july-2024-operation/delta-pauses-global-flight-schedule` | Delta July 19–24, 2024 operation updates | 2024-07-19 to 2024-07-24 | 2026-07-21 | Generator acceptance gates and Delta tenant incident eras | citeturn5search3turn5search0turn5search5 |
| `ascension_cyber_may_2024` | `primary_verified` | Ascension | `https://about.ascension.org/news/2024/05/network-interruption-update2` | Ascension network interruption and FY24/FY25 recovery disclosures | 2024-05-08 onward | 2026-07-21 | Generator acceptance gates and Ascension downtime recovery eras | citeturn6search3turn6search0turn6search2 |
| `mgm_cyber_sep_2023` | `primary_verified` | MGM Resorts Investor Relations | `https://investors.mgmresorts.com/2023-09-12-MGM-RESORTS-INTERNATIONAL-STATEMENT-ON-CYBERSECURITY-ISSUE` | MGM cybersecurity issue statements | 2023-09-12 and 2023-10-05 | 2026-07-21 | Generator acceptance gates and MGM downtime eras | citeturn5search1turn5search2 |
| `who_pandemic_2020` | `primary_verified` | WHO | `https://www.who.int/news-room/speeches/item/who-director-general-s-opening-remarks-at-the-media-briefing-on-covid-19---11-march-2020` | WHO pandemic characterization | 2020-03-11 | 2026-07-21 | Cross-tenant 2020 scenario baseline | citeturn25search0turn25search8 |
| `delta_alpa_contract_2023` | `design_heuristic` | ALPA | `https://www.alpa.org/press-room/2023/delta-pilots-approve-new-contract` | Delta pilots approve new contract | 2023-03-01 | 2026-07-21 | Scenario shaping only; no frozen pay rules without executed CBA ingest | citeturn29search0 |
| `culinary_mgm_contract_pack` | `design_heuristic` | Culinary Union Local 226 | `https://www.culinaryunion226.org/news/press/culinary-union-reaches-a-tentative-agreement-with-the-cosmopolitan-las-vegas-on-a-new-3-year-contract` | Public union summaries | 2025-05-24 and related public notices | 2026-07-21 | Scenario shaping only; no frozen thresholds without executed property-specific CBA ingest | citeturn29search2turn29search5 |

**Tenant constitutions**

**Delta Air Lines**

Hierarchy:
```yaml
tenant_id: delta
primary_project: P03
supporting_projects: [P01, P02, P04, P05]
hierarchy:
  enterprise: "Delta Air Lines"
  divisions: ["Flight Operations", "Airport Customer Service", "TechOps", "Crew Resources"]
  operational_nodes:
    airports: "all_us_airports"
    crew_bases: "all_us_crew_bases"
    hubs: ["ATL", "MSP", "DTW", "SLC", "LAX", "JFK", "SEA", "BOS"]
```

Jurisdiction packs and frozen invariant spine:
```yaml
jurisdiction_packs:
  - faa_part_117
  - faa_ac_117_2
  - flsa_hours_worked
  - state_wage_hour_pack[*]
frozen_invariant_spine:
  - code: DELTA-FDP-001
    rule: "No dispatched duty may exceed Part 117 tables once acclimation, augmentation, split duty, and extensions are resolved."
    source: faa_part_117
  - code: DELTA-REST-001
    rule: "Required rest and cumulative lookback checks must pass before legality-green publication."
    source: faa_part_117
  - code: DELTA-FRMS-001
    rule: "Any FRMS override path requires recorded fatigue-report channel, evaluator separation, and dual approval."
    source: faa_part_117
  - code: DELTA-PAY-001
    rule: "No payroll publication from incident mode without a Decision Passport and outbox bundle hash."
    source: flsa_hours_worked
contractual_thresholds:
  status: design_heuristic_until_executed_cba_ingested
```

Scenario eras, intensity curves, and expected signatures:
```yaml
scenario_eras:
  - era: 2016_2019_network_baseline
    intensity_curve: {seasonality: "high", irregular_ops: "weather-driven pulses", manual_capture: "low"}
    expected_signatures:
      crew_swap_ratio: "baseline"
      legality_near_miss_rate: "baseline"
      timezone_crossings: "stable high"
  - era: 2020_grounding_and_furlough
    trigger: "WHO pandemic characterization 2020-03-11"
    intensity_curve: {operation_volume: "sharp down", status_change_volume: "extreme up", manual_reassignment: "high"}
    expected_signatures:
      inactive_employee_ratio: "> baseline"
      retro_pay_adjustments: "> baseline"
      training_recurrency_backlog: "> baseline"
  - era: 2021_2022_recovery_surge
    intensity_curve: {operation_volume: "sharp up", recovery_irregular_ops: "high", reserve_usage: "high"}
    expected_signatures:
      open_trip_fill_latency: "<= compressed"
      reserve_conversion_rate: "> baseline"
      duty_extension_requests: "> baseline"
  - era: 2023_contract_enforcement
    intensity_curve: {schedule_rule_variance: "medium", bid_line_rebuilds: "medium"}
    expected_signatures:
      pairing_reprice_events: "> baseline"
      quality_of_life_exception_codes: "> baseline"
  - era: 2024_crowdstrike_window
    trigger: "2024-07-19 to 2024-07-24"
    intensity_curve: {crew_system_disruption: "extreme", manual_support: "extreme", reconciliation_load: "extreme"}
    expected_signatures:
      manual_crew_assignment_multiplier: ">= 4.0"
      legality_hold_queue_multiplier: ">= 3.0"
      downstream_payroll_delta_batches: ">= 2.0"
  - era: 2025_2026_stabilization
    intensity_curve: {irregular_ops: "normalizing", FRMS_tuning: "higher", manual_support: "reduced"}
```

The 2024 Delta disruption window is frozen into the scenario engine because Delta publicly paused its schedule on July 19, 2024, then described Crew Tracking as one of the most complex systems requiring manual support before operations materially normalized on July 24, 2024. citeturn5search3turn5search0turn5search5

Pain channel and dual-key rules: any legality-red crew pairing, fatigue-report-triggered duty continuation, mass manual reassignment, or payroll-impacting duty reconstruction opens the algadonic channel immediately to the tenant incident commander and the safety/payroll domain owner. The system may contain action space, but it may not silently command an override. That containment-first choice is transcript-mandated. fileciteturn0file0L1518-L1531 fileciteturn0file0L8061-L8076

Required Decision Passport classes:
```yaml
decision_passport_classes:
  - crew_legality_evaluation
  - fatigue_override_request
  - manual_crew_reconstruction
  - irregular_ops_pay_protection
  - schedule_republish_after_incident
```

**Ascension Healthcare**

Hierarchy:
```yaml
tenant_id: ascension
primary_project: P02
supporting_projects: [P01, P03, P04, P05]
hierarchy:
  enterprise: "Ascension"
  divisions: ["Hospitals", "Medical Groups", "Ambulatory", "Shared Services"]
  operational_nodes:
    regions: "all_ascension_regions"
    hospitals: "all_hospitals"
    units: ["ED", "ICU", "MedSurg", "OR", "L&D", "Float Pool"]
```

Jurisdiction packs and frozen invariant spine:
```yaml
jurisdiction_packs:
  - cms_482_23
  - nlc_compact
  - flsa_hours_worked
  - flsa_healthcare_hours
  - hipaa_security_pack
  - state_board_of_nursing_pack[*]
frozen_invariant_spine:
  - code: ASC-NURSE-001
    rule: "Every staffed inpatient unit must resolve to valid and current licensure for every role that requires licensure."
    source: cms_482_23
  - code: ASC-NURSE-002
    rule: "RN supervision requirements and nursing-care assignment must be provable in the passport if staffing substitutions occur."
    source: cms_482_23
  - code: ASC-PAY-001
    rule: "Compensable time, rounding, and off-the-clock checks must execute before payroll publication."
    source: flsa_hours_worked
  - code: ASC-DOWNTIME-001
    rule: "Downtime payroll recovery must preserve employee pay via provisional-presence wage protection until reconciliation completes."
    source: flsa_hours_worked
staffing_ratios:
  status: design_heuristic_or_state_pack_specific
```

Scenario eras and signatures:
```yaml
scenario_eras:
  - era: 2016_2019_baseline
    intensity_curve: {patient_volume: "baseline", credential_drift: "low", manual_capture: "low"}
  - era: 2020_2021_pandemic_surge
    trigger: "WHO pandemic characterization 2020-03-11"
    intensity_curve: {icu_load: "extreme", overtime: "extreme", agency_usage: "high"}
    expected_signatures:
      premium_pay_mix: "> baseline"
      shift_extensions: "> baseline"
      credential_float_checks: "> baseline"
  - era: 2022_travel_nurse_and_stabilization
    intensity_curve: {external_labor_mix: "high", local_orientation: "high"}
    expected_signatures:
      agency_assignment_ratio: "> baseline"
      badge_photo_quality_variance: "> baseline"
  - era: 2024_cyber_downtime
    trigger: "2024-05-08 onward"
    intensity_curve: {manual_documentation: "extreme", retro_adjustment: "extreme", reconciliation: "extreme"}
    expected_signatures:
      manual_punch_multiplier: ">= 5.0"
      retro_timecard_edits: ">= 4.0"
      delta_batch_publications: ">= 3.0"
  - era: 2025_2026_recovery
    intensity_curve: {volume_recovery: "medium-high", data_restoration: "high"}
```

Ascension disclosed on May 8, 2024 that a cybersecurity event interrupted access to parts of its technology network, and later disclosed that May and June 2024 operations were materially affected by business interruption and remediation costs. It also disclosed FY25 recovery in same-facility volume after the attack. Those disclosures are strong enough to force non-random downtime and retro-correction behavior into the generator and the architecture. citeturn6search3turn6search0turn6search2turn6search4

Pain channel and dual-key rules: nurse licensure invalid at assignment time, RN-supervision failure, downtime payroll publication with unresolved provenance gaps, and patient-care staffing exceptions all require dual approval by the clinical operations owner and payroll/reconciliation owner. When the worker-harm channel fires, dashboards are bypassed and publication is held.

Required Decision Passport classes:
```yaml
decision_passport_classes:
  - patient_unit_staffing_exception
  - downtime_manual_entry_attestation
  - retro_payroll_correction
  - credential_expiry_override
  - provisional_presence_wage_protection
```

**MGM Resorts Las Vegas**

Hierarchy:
```yaml
tenant_id: mgm_lv
primary_project: P01
supporting_projects: [P02, P03, P04, P05]
hierarchy:
  enterprise: "MGM Resorts Las Vegas"
  divisions: ["Casino Operations", "Hotel Operations", "Food and Beverage", "Entertainment", "Security"]
  operational_nodes:
    properties: "all_vegas_locations"
    sublocations: ["casino_floor", "pit", "hotel_tower", "kitchen", "restaurant", "back_of_house"]
```

Jurisdiction packs and frozen invariant spine:
```yaml
jurisdiction_packs:
  - nevada_overtime
  - nevada_tips
  - flsa_hours_worked
  - culinary_union_pack[design_heuristic]
frozen_invariant_spine:
  - code: MGM-OT-001
    rule: "Nevada daily and weekly overtime must be computed from resolved role-segmented hours, not shift shell assumptions."
    source: nevada_overtime
  - code: MGM-TIP-001
    rule: "Tips may not be credited toward the statutory wage floor and employer retention is prohibited."
    source: nevada_tips
  - code: MGM-MULTIROLE-001
    rule: "A single physical shift with multiple roles must publish as segmented labor context before payroll."
    source: flsa_hours_worked
  - code: MGM-DOWNTIME-001
    rule: "Cyber/manual capture mode cannot suppress worker pay; provisional-presence wage protection applies."
    source: flsa_hours_worked
```

Scenario eras and signatures:
```yaml
scenario_eras:
  - era: 2016_2019_strip_baseline
    intensity_curve: {occupancy: "high cyclical", weekend_premium: "high", manual_capture: "low"}
  - era: 2020_strip_closure_and_reopen
    trigger: "2020-03-17 closure; phased reopen through 2020-09-30"
    intensity_curve: {active_headcount: "collapsed then staged recovery", reactivation_events: "extreme"}
    expected_signatures:
      inactive_status_ratio: "> baseline"
      callback_rehire_events: "> baseline"
      occupancy_labor_decoupling: "spike"
  - era: 2021_2022_recovery
    intensity_curve: {weekend_peaks: "high", event_staffing: "rebound"}
  - era: 2023_cyber_downtime
    trigger: "2023-09-11 to 2023-10-05 recovery period"
    intensity_curve: {manual_capture: "extreme", exception_flags: "extreme", reconciliation: "high"}
    expected_signatures:
      manual_punch_share: ">= 6.0x"
      manager_attestation_volume: ">= 5.0x"
      retro_tip_pool_reallocations: ">= 2.0x"
  - era: 2024_2026_contract_and_technology_tightening
    intensity_curve: {multi_role_segmentation: "high", tech_language_exceptions: "medium"}
```

MGM publicly announced temporary closure of Las Vegas properties effective March 17, 2020, then disclosed phased reopenings that ran through September 30, 2020. MGM also disclosed the September 2023 cybersecurity issue and later said an unauthorized party obtained customer data on September 11, 2023. That makes closure/reactivation waves and cyber/manual capture spikes mandatory scenario anchors. citeturn7search0turn7search3turn7search1turn5search1turn5search2

Pain channel and dual-key rules: any tip-pool redistribution after manual downtime, any daily-overtime exception that crosses a role boundary, and any missing-edge-capture cluster above property threshold opens the pain channel to labor operations and payroll. Public union releases remain design heuristics until property-level executed CBAs are ingested.

Required Decision Passport classes:
```yaml
decision_passport_classes:
  - edge_capture_exception
  - multi_role_shift_segmentation
  - tip_pool_reconstruction
  - manual_timecard_backfill
  - daily_overtime_exception
```

**Schneider Electric**

Hierarchy:
```yaml
tenant_id: schneider
primary_project: P04
supporting_projects: [P01, P02, P03, P05]
hierarchy:
  enterprise: "Schneider Electric"
  divisions: ["Manufacturing", "Field Services", "Digital Energy", "Supply Chain"]
  operational_nodes:
    plants: "all_locations"
    work_centers: ["assembly", "test", "maintenance", "warehouse", "field_service"]
```

Jurisdiction packs and frozen invariant spine:
```yaml
jurisdiction_packs:
  - osha_1910_147
  - osha_1910_269
  - flsa_hours_worked
  - gdpr_article_9
  - ico_worker_biometrics
  - local_labor_pack[*]
frozen_invariant_spine:
  - code: SCH-QUAL-001
    rule: "No assignment to hazardous-energy work without current qualification and energy-control authorization."
    source: osha_1910_147
  - code: SCH-QUAL-002
    rule: "No assignment to electric-power operations without role-qualified personnel and clearance constraints."
    source: osha_1910_269
  - code: SCH-GRAPH-001
    rule: "Qualification graph edges must be effective-dated, source-ranked, and revocation-aware."
    source: osha_1910_147
  - code: SCH-PRIV-001
    rule: "If biometrics are used in any non-U.S. site, lawful basis, alternative path, DPIA, and minimization controls are mandatory."
    source: gdpr_article_9
```

Scenario eras and signatures:
```yaml
scenario_eras:
  - era: 2016_2019_baseline
    intensity_curve: {skills_variance: "medium", overtime: "seasonal"}
  - era: 2020_pandemic_volatility
    intensity_curve: {supplier_delay: "high", on_site_access_change: "high"}
  - era: 2021_2022_supply_constraint_and_transition
    intensity_curve: {qualification_reassignment: "high", alternate_sourcing: "high", maintenance_window_pressure: "high"}
    expected_signatures:
      substitute_bom_skill_mappings: "> baseline"
      maintenance_reschedule_rate: "> baseline"
  - era: 2022_2026_electrification_growth
    trigger: "post-IRA clean energy credit regime and Schneider transition demand"
    intensity_curve: {specialized_skill_demand: "upward", training_load: "upward"}
    expected_signatures:
      certification_queue_length: "> baseline"
      cross-plant_skill_sharing: "> baseline"
```

Schneider publicly framed 2022 as a year of geopolitical and economic uncertainty while continuing to expand decarbonization and electrification activity, and the U.S. IRA and related tax-credit implementation increased industrial demand around clean energy manufacturing and infrastructure. Those facts justify a non-random increase in qualification churn, training demand, and supply-chain rescheduling after 2022. citeturn27search1turn28search2turn28search4

Pain channel and dual-key rules: any assignment proposal that would place an unqualified worker into lockout/tagout or electric-power work is a hard stop. No local manager may suppress the alert. The approval pair is site safety owner plus tenant qualification-owner.

Required Decision Passport classes:
```yaml
decision_passport_classes:
  - qualification_resolution
  - hazardous_energy_authorization
  - electrical_clearance_assignment
  - cross_plant_skill_substitution
  - biometric_enrichment_opt_in
```

**PepsiCo**

Hierarchy:
```yaml
tenant_id: pepsico
primary_project: P05
supporting_projects: [P01, P02, P03, P04]
hierarchy:
  enterprise: "PepsiCo"
  divisions: ["Beverage Manufacturing", "Foods Manufacturing", "Distribution", "Warehousing"]
  operational_nodes:
    locations: "all_locations"
    frontline_domains: ["plant", "dc", "yard", "route_dispatch", "warehouse"]
```

Jurisdiction packs and frozen invariant spine:
```yaml
jurisdiction_packs:
  - illinois_bipa
  - texas_biometric_503_001
  - washington_biometrics_19_375
  - gdpr_article_9
  - ico_worker_biometrics
  - flsa_hours_worked
  - fmcsa_hos_summary
  - state_labor_pack[*]
frozen_invariant_spine:
  - code: PEP-BIO-001
    rule: "Face-only template creation requires jurisdiction-appropriate notice, lawful basis, and retention/destruction policy."
    source: illinois_bipa
  - code: PEP-BIO-002
    rule: "Alternative non-biometric path is mandatory where consent is relied on or where biometric processing would otherwise disadvantage the worker."
    source: ico_worker_biometrics
  - code: PEP-BIO-003
    rule: "No raw facial image persistence in operational stores; only purpose-bound encrypted templates or derived confidence artifacts."
    source: gdpr_article_9
  - code: PEP-PAY-001
    rule: "Recognition uncertainty must create provisional-presence wage protection rather than lost time."
    source: flsa_hours_worked
  - code: PEP-HOS-001
    rule: "If a worker stream is DOT-governed, HOS checks execute before dispatch-linked publication."
    source: fmcsa_hos_summary
```

Scenario eras and signatures:
```yaml
scenario_eras:
  - era: 2016_2019_baseline
    intensity_curve: {summer_beverage_peak: "high", weekend_dc_overtime: "medium", biometric_exception_rate: "low"}
  - era: 2020_2021_supply_chain_and_restriction_stress
    trigger: "WHO pandemic era and complex value-chain disruption"
    intensity_curve: {dc_overtime: "high", route_resequencing: "high", manual_fallback: "high"}
    expected_signatures:
      missed_meal_flag_rate: "> baseline"
      overtime_limit_proximity: "> baseline"
      temporary_access_method_usage: "> baseline"
  - era: 2022_renewable_and_value_chain_transition
    trigger: "PepsiCo/Schneider value-chain program"
    intensity_curve: {supplier_variability: "medium", site_security_policy_updates: "medium"}
  - era: 2023_2026_biometric_governance_tightening
    intensity_curve: {consent_refresh: "high in covered jurisdictions", opt_out_rate: "non-zero and stable"}
    expected_signatures:
      alternate_authentication_share: ">= jurisdiction floor"
      dpia_completion_rate: "100%"
      template_destruction_sla: "met"
```

PepsiCo’s public materials describe a complex value chain and a tumultuous 2020 operating context, and PepsiCo and Schneider publicly announced a value-chain renewable-electricity initiative in 2022. The legal backbone for face-only time capture is much stricter: Illinois BIPA requires public retention policy and notice/consent elements; Texas requires informed consent plus destruction within a bounded period; Washington regulates commercial enrollment, disclosure, and retention; GDPR treats biometric data used for unique identification as special-category data; and the ICO says workplace biometric access/time systems need DPIAs, alternatives, manual review paths, and no detriment for workers who opt for the alternative. citeturn26search0turn27search5turn15search6turn21search1turn17search6turn16search1turn16search0turn16search2

Pain channel and dual-key rules: false-non-match spikes, denied-entry without alternative path, template-retention breach, or payroll loss from biometric uncertainty all open the pain channel directly to privacy/compliance and payroll operations. No manager override may disable the alternative authentication path.

Required Decision Passport classes:
```yaml
decision_passport_classes:
  - biometric_enrollment
  - alternative_authentication_invocation
  - provisional_presence_creation
  - geofence_exception_resolution
  - template_deletion_and_reconsent
```

## Control-plane schemas

**Shared control-plane artifacts**

The constitution publishes the following first-class artifacts and treats prose as explanatory only:

```yaml
artifacts:
  - decision-passport.schema.json
  - evidence-envelope.schema.json
  - autonomy-envelope.schema.json
  - worker-harm-signal-catalog.yaml
  - architecture-evolution-ledger.schema.json
  - scenario-calendar.yaml
  - frozen-invariants.yaml
```

**`decision-passport.schema.json`**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:ukg:assurance:decision-passport.schema.json",
  "title": "DecisionPassport",
  "type": "object",
  "required": [
    "schema_version",
    "passport_id",
    "tenant_id",
    "project_id",
    "decision_class",
    "status",
    "subject_refs",
    "event_window",
    "evidence",
    "anchors",
    "invariant_checks",
    "writer",
    "evaluator",
    "approval_chain",
    "action",
    "observed_ukg_state",
    "payroll_publication",
    "reconciliation",
    "assurance"
  ],
  "properties": {
    "schema_version": { "type": "string", "const": "1.0.0" },
    "passport_id": { "type": "string", "pattern": "^dp_[a-z0-9]{26}$" },
    "tenant_id": { "type": "string", "enum": ["delta", "ascension", "mgm_lv", "schneider", "pepsico"] },
    "project_id": { "type": "string", "enum": ["P01", "P02", "P03", "P04", "P05"] },
    "decision_class": { "type": "string", "minLength": 3 },
    "status": { "type": "string", "enum": ["draft", "evaluated", "approved", "executed", "observed", "reconciled", "quarantined", "superseded"] },
    "subject_refs": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/SubjectRef" }
    },
    "event_window": { "$ref": "#/$defs/EventWindow" },
    "evidence": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/EvidenceRef" }
    },
    "anchors": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/AnchorRef" }
    },
    "anchor_integrity_avg": { "type": "number", "minimum": 0, "maximum": 1 },
    "invariant_checks": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/InvariantCheck" }
    },
    "writer": { "$ref": "#/$defs/AgentOrHuman" },
    "evaluator": { "$ref": "#/$defs/AgentOrHuman" },
    "approval_chain": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/ApprovalStep" }
    },
    "autonomy_envelope_ref": { "type": "string", "pattern": "^ae_[a-z0-9]{26}$" },
    "action": { "$ref": "#/$defs/ActionBlock" },
    "observed_ukg_state": { "$ref": "#/$defs/ObservedState" },
    "payroll_publication": { "$ref": "#/$defs/PayrollPublication" },
    "reconciliation": { "$ref": "#/$defs/ReconciliationBlock" },
    "worker_harm_signals": {
      "type": "array",
      "items": { "$ref": "#/$defs/WorkerHarmSignal" }
    },
    "assurance": { "$ref": "#/$defs/AssuranceBlock" },
    "hash_chain": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/HashLink" }
    }
  },
  "$defs": {
    "UUIDishTime": { "type": "string", "format": "date-time" },
    "SubjectRef": {
      "type": "object",
      "required": ["kind", "id"],
      "properties": {
        "kind": { "type": "string", "enum": ["employee", "assignment", "timecard", "shift", "route", "qualification", "property", "unit", "device"] },
        "id": { "type": "string", "minLength": 1 },
        "effective_at": { "$ref": "#/$defs/UUIDishTime" }
      },
      "additionalProperties": false
    },
    "EventWindow": {
      "type": "object",
      "required": ["occurred_start", "occurred_end", "business_dates"],
      "properties": {
        "occurred_start": { "$ref": "#/$defs/UUIDishTime" },
        "occurred_end": { "$ref": "#/$defs/UUIDishTime" },
        "business_dates": {
          "type": "array",
          "minItems": 1,
          "items": { "type": "string", "format": "date" }
        },
        "timezone_context": { "type": "array", "items": { "type": "string" } }
      },
      "additionalProperties": false
    },
    "EvidenceRef": {
      "type": "object",
      "required": ["evidence_id", "envelope_id", "source_system", "kind", "sha256"],
      "properties": {
        "evidence_id": { "type": "string", "pattern": "^ev_[a-z0-9]{26}$" },
        "envelope_id": { "type": "string", "pattern": "^ee_[a-z0-9]{26}$" },
        "source_system": { "type": "string" },
        "kind": { "type": "string", "enum": ["punch", "schedule", "assignment", "attestation", "webhook", "api_pull", "batch_file", "sensor", "manual_entry", "payroll_ack"] },
        "sha256": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
        "anchor_candidate": { "type": "boolean" }
      },
      "additionalProperties": false
    },
    "AnchorRef": {
      "type": "object",
      "required": ["anchor_id", "anchor_type", "integrity_score", "independence_class"],
      "properties": {
        "anchor_id": { "type": "string", "pattern": "^an_[a-z0-9]{26}$" },
        "anchor_type": { "type": "string", "enum": ["physical_capture", "runtime_receipt", "signed_ack", "device_attestation", "external_status", "human_attestation_dual", "observed_ukg_state"] },
        "integrity_score": { "type": "number", "minimum": 0, "maximum": 1 },
        "independence_class": { "type": "string", "enum": ["independent", "semi_independent", "entangled"] },
        "degradation_reason": { "type": ["string", "null"] }
      },
      "additionalProperties": false
    },
    "InvariantCheck": {
      "type": "object",
      "required": ["invariant_code", "bundle_hash", "result", "source_status"],
      "properties": {
        "invariant_code": { "type": "string" },
        "bundle_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
        "result": { "type": "string", "enum": ["pass", "fail", "not_applicable", "manual_review_required"] },
        "source_status": { "type": "string", "enum": ["primary_verified", "design_heuristic"] },
        "detail_ref": { "type": ["string", "null"] }
      },
      "additionalProperties": false
    },
    "AgentOrHuman": {
      "type": "object",
      "required": ["actor_type", "actor_id"],
      "properties": {
        "actor_type": { "type": "string", "enum": ["human", "agent", "service"] },
        "actor_id": { "type": "string" },
        "model_or_role": { "type": ["string", "null"] }
      },
      "additionalProperties": false
    },
    "ApprovalStep": {
      "type": "object",
      "required": ["step", "approver", "decision", "decided_at"],
      "properties": {
        "step": { "type": "string" },
        "approver": { "$ref": "#/$defs/AgentOrHuman" },
        "decision": { "type": "string", "enum": ["approved", "rejected", "escalated"] },
        "decided_at": { "$ref": "#/$defs/UUIDishTime" },
        "dual_key_group": { "type": ["string", "null"] }
      },
      "additionalProperties": false
    },
    "ActionBlock": {
      "type": "object",
      "required": ["action_type", "requested_changes"],
      "properties": {
        "action_type": { "type": "string", "enum": ["hold", "publish", "correct", "override", "recover", "quarantine", "replay", "reassign"] },
        "requested_changes": { "type": "array", "items": { "type": "string" } },
        "rollback_plan_ref": { "type": ["string", "null"] }
      },
      "additionalProperties": false
    },
    "ObservedState": {
      "type": "object",
      "required": ["ukg_object_refs", "observed_at", "state_hash"],
      "properties": {
        "ukg_object_refs": { "type": "array", "items": { "type": "string" } },
        "observed_at": { "$ref": "#/$defs/UUIDishTime" },
        "state_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
      },
      "additionalProperties": false
    },
    "PayrollPublication": {
      "type": "object",
      "required": ["publication_state", "outbox_key"],
      "properties": {
        "publication_state": { "type": "string", "enum": ["not_started", "prepared", "validated", "signed", "queued", "transmitted", "acknowledged", "applied", "corrected", "blocked"] },
        "outbox_key": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
        "bundle_hash": { "type": ["string", "null"], "pattern": "^[a-f0-9]{64}$" }
      },
      "additionalProperties": false
    },
    "ReconciliationBlock": {
      "type": "object",
      "required": ["status", "wage_protection_applied"],
      "properties": {
        "status": { "type": "string", "enum": ["pending", "complete", "partial", "quarantined"] },
        "wage_protection_applied": { "type": "boolean" },
        "delta_batch_refs": { "type": "array", "items": { "type": "string" } }
      },
      "additionalProperties": false
    },
    "WorkerHarmSignal": {
      "type": "object",
      "required": ["signal_code", "severity", "opened_at"],
      "properties": {
        "signal_code": { "type": "string" },
        "severity": { "type": "string", "enum": ["medium", "high", "critical"] },
        "opened_at": { "$ref": "#/$defs/UUIDishTime" },
        "closed_at": { "type": ["string", "null"], "format": "date-time" }
      },
      "additionalProperties": false
    },
    "AssuranceBlock": {
      "type": "object",
      "required": ["passport_completeness", "anchor_integrity_avg", "assurance_score"],
      "properties": {
        "passport_completeness": { "type": "number", "minimum": 0, "maximum": 100 },
        "anchor_integrity_avg": { "type": "number", "minimum": 0, "maximum": 100 },
        "assurance_score": { "type": "number", "minimum": 0, "maximum": 100 },
        "cross_tenant_isolation_passed": { "type": "boolean" }
      },
      "additionalProperties": false
    },
    "HashLink": {
      "type": "object",
      "required": ["kind", "sha256"],
      "properties": {
        "kind": { "type": "string" },
        "sha256": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

**`evidence-envelope.schema.json`**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:ukg:assurance:evidence-envelope.schema.json",
  "title": "EvidenceEnvelope",
  "type": "object",
  "required": [
    "schema_version",
    "envelope_id",
    "tenant_id",
    "received_at",
    "source",
    "payload_sha256",
    "provenance",
    "evidence_corruption_checks"
  ],
  "properties": {
    "schema_version": { "type": "string", "const": "1.0.0" },
    "envelope_id": { "type": "string", "pattern": "^ee_[a-z0-9]{26}$" },
    "tenant_id": { "type": "string" },
    "received_at": { "type": "string", "format": "date-time" },
    "source": {
      "type": "object",
      "required": ["system", "channel", "message_id"],
      "properties": {
        "system": { "type": "string" },
        "channel": { "type": "string", "enum": ["webhook", "api_pull", "batch", "manual", "sensor", "derived"] },
        "message_id": { "type": "string" },
        "replay_of": { "type": ["string", "null"] }
      },
      "additionalProperties": false
    },
    "payload_sha256": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "provenance": {
      "type": "object",
      "required": ["signature_state", "clock_state"],
      "properties": {
        "signature_state": { "type": "string", "enum": ["verified", "missing", "invalid", "not_applicable"] },
        "clock_state": { "type": "string", "enum": ["trusted", "untrusted", "derived"] },
        "device_attestation": { "type": ["string", "null"] }
      },
      "additionalProperties": false
    },
    "evidence_corruption_checks": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["mode", "result"],
        "properties": {
          "mode": { "type": "string", "enum": ["filtering", "entanglement", "construction", "performance"] },
          "result": { "type": "string", "enum": ["clear", "suspect", "quarantine"] }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

**`autonomy-envelope.schema.json`**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:ukg:assurance:autonomy-envelope.schema.json",
  "title": "AutonomyEnvelope",
  "type": "object",
  "required": [
    "schema_version",
    "autonomy_envelope_id",
    "tenant_id",
    "executor_class",
    "allowed_actions",
    "forbidden_actions",
    "budget",
    "human_interlocks",
    "rollback_requirements"
  ],
  "properties": {
    "schema_version": { "type": "string", "const": "1.0.0" },
    "autonomy_envelope_id": { "type": "string", "pattern": "^ae_[a-z0-9]{26}$" },
    "tenant_id": { "type": "string" },
    "executor_class": { "type": "string", "enum": ["analysis_agent", "repair_agent", "publication_agent", "replay_agent"] },
    "allowed_actions": { "type": "array", "items": { "type": "string" } },
    "forbidden_actions": {
      "type": "array",
      "items": { "type": "string" },
      "contains": { "const": "cross_tenant_read" }
    },
    "budget": {
      "type": "object",
      "required": ["max_minutes", "max_api_calls", "max_write_sets"],
      "properties": {
        "max_minutes": { "type": "integer", "minimum": 1 },
        "max_api_calls": { "type": "integer", "minimum": 1 },
        "max_write_sets": { "type": "integer", "minimum": 0 }
      },
      "additionalProperties": false
    },
    "human_interlocks": {
      "type": "array",
      "items": { "type": "string", "enum": ["payroll_publication", "safety_override", "tenant_boundary_change", "frozen_invariant_change", "manual_identity_resolution"] }
    },
    "rollback_requirements": {
      "type": "object",
      "required": ["plan_required", "dry_run_required"],
      "properties": {
        "plan_required": { "type": "boolean" },
        "dry_run_required": { "type": "boolean" }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

**`worker-harm-signal-catalog.yaml`**
```yaml
version: 1.0.0
signals:
  - code: WHS_PAY_LOSS_RISK
    severity: critical
    opens_pain_channel: true
    description: Employee may lose earned pay due to capture, interpretation, or publication failure.
  - code: WHS_LEGALITY_BREACH_RISK
    severity: critical
    opens_pain_channel: true
    description: Regulated duty/rest or qualification rule may be violated.
  - code: WHS_ACCESS_DENIAL_AUTOMATION
    severity: high
    opens_pain_channel: true
    description: Worker denied entry/start due to biometric or automated decision failure without reviewed fallback.
  - code: WHS_CREDENTIAL_INVALID_ASSIGNMENT
    severity: critical
    opens_pain_channel: true
    description: Planned or performed assignment lacks required active credential.
  - code: WHS_DOWNTIME_MANUAL_BACKFILL
    severity: high
    opens_pain_channel: false
    description: Manual reconstruction volume exceeds tenant threshold and requires attestation chain.
  - code: WHS_TIP_POOL_DISTORTION
    severity: high
    opens_pain_channel: true
    description: Manual or algorithmic change may distort employee-owned gratuities.
```

**`architecture-evolution-ledger.schema.json`**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:ukg:assurance:architecture-evolution-ledger.schema.json",
  "title": "ArchitectureEvolutionLedgerEntry",
  "type": "object",
  "required": [
    "schema_version",
    "change_id",
    "change_type",
    "proposed_by",
    "source_proof",
    "affected_artifacts",
    "dual_control",
    "regression_suite",
    "activation_plan",
    "rollback_package"
  ],
  "properties": {
    "schema_version": { "type": "string", "const": "1.0.0" },
    "change_id": { "type": "string", "pattern": "^ael_[a-z0-9]{26}$" },
    "change_type": { "type": "string", "enum": ["frozen_invariant_change", "schema_change", "generator_change", "rls_change", "threat_model_change"] },
    "proposed_by": { "type": "string" },
    "source_proof": {
      "type": "array",
      "minItems": 1,
      "items": { "type": "string" }
    },
    "affected_artifacts": { "type": "array", "items": { "type": "string" } },
    "dual_control": {
      "type": "object",
      "required": ["domain_owner", "platform_owner", "approved"],
      "properties": {
        "domain_owner": { "type": "string" },
        "platform_owner": { "type": "string" },
        "approved": { "type": "boolean" }
      },
      "additionalProperties": false
    },
    "regression_suite": {
      "type": "object",
      "required": ["held_out_suite_id", "passed"],
      "properties": {
        "held_out_suite_id": { "type": "string" },
        "passed": { "type": "boolean" }
      },
      "additionalProperties": false
    },
    "activation_plan": {
      "type": "object",
      "required": ["not_before", "canary_scope"],
      "properties": {
        "not_before": { "type": "string", "format": "date-time" },
        "canary_scope": { "type": "string" }
      },
      "additionalProperties": false
    },
    "rollback_package": {
      "type": "object",
      "required": ["artifact_hash", "restore_steps"],
      "properties": {
        "artifact_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
        "restore_steps": { "type": "array", "items": { "type": "string" } }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

**`scenario-calendar.yaml` shared core with tenant overlays**
```yaml
version: 1.0.0
shared:
  defaults:
    intensity_scale: [0, 1, 2, 3, 4, 5]
    anomaly_types:
      - manual_capture_spike
      - overtime_spike
      - hazard_pay_window
      - furlough_status_churn
      - cyber_downtime
      - credential_drift
      - supply_chain_delay
      - weather_irregular_ops
      - payroll_delta_batch
  required_signature_fields:
    - manual_entry_share
    - overtime_hours
    - exception_rate
    - retro_adjustment_count
    - attestation_volume
    - schedule_change_rate

overlays:
  delta:
    eras:
      - id: delta_2024_crowdstrike
        window: {start: "2024-07-19", end: "2024-07-24"}
        intensity:
          manual_capture_spike: 5
          weather_irregular_ops: 1
          payroll_delta_batch: 4
        anomaly_payload:
          cause: "crew-system outage and manual synchronization"
          expected_signatures:
            manual_entry_share: {multiplier_min: 4.0}
            legality_hold_queue: {multiplier_min: 3.0}
            payroll_delta_batch: {multiplier_min: 2.0}
  ascension:
    eras:
      - id: asc_2024_cyber
        window: {start: "2024-05-08", end: "2024-06-30"}
        intensity:
          cyber_downtime: 5
          manual_capture_spike: 5
          payroll_delta_batch: 5
        anomaly_payload:
          cause: "network interruption and manual documentation"
          expected_signatures:
            manual_entry_share: {multiplier_min: 5.0}
            retro_adjustment_count: {multiplier_min: 4.0}
  mgm_lv:
    eras:
      - id: mgm_2023_cyber
        window: {start: "2023-09-11", end: "2023-10-05"}
        intensity:
          cyber_downtime: 5
          manual_capture_spike: 5
          payroll_delta_batch: 4
        anomaly_payload:
          cause: "property-system cyber disruption"
          expected_signatures:
            manual_entry_share: {multiplier_min: 6.0}
            manager_attestation_volume: {multiplier_min: 5.0}
  schneider:
    eras:
      - id: sch_2022_electrification_pull
        window: {start: "2022-08-16", end: "2026-12-31"}
        intensity:
          supply_chain_delay: 3
          credential_drift: 3
        anomaly_payload:
          cause: "clean-energy and electrification demand expansion"
          expected_signatures:
            certification_queue_length: {multiplier_min: 1.5}
  pepsico:
    eras:
      - id: pep_2020_supply_chain_stress
        window: {start: "2020-03-11", end: "2021-12-31"}
        intensity:
          supply_chain_delay: 4
          overtime_spike: 4
          manual_capture_spike: 3
        anomaly_payload:
          cause: "pandemic-era value-chain disruption"
          expected_signatures:
            overtime_hours: {multiplier_min: 1.6}
            exception_rate: {multiplier_min: 1.5}
```

This calendar is deterministic on purpose. The generator is forbidden from uniform-random histories because the transcript corpus is explicit that reliability lives in the mediation layer, in verification, in trace compression, and in comparative measurement of workflow variants rather than in producing plausible-looking noise. fileciteturn0file0L539-L544 fileciteturn0file0L554-L566 fileciteturn0file0L593-L606 fileciteturn0file0L614-L623

## Database and integration contracts

**Database isolation specification**

The data store is tenant-first, date-second, and claim-scoped. The tenant boundary is not logical-only; it is structural. Every large fact table uses **LIST (`tenant_id`)** at the first partition level and **RANGE (`business_date`)** at the second. Analysts never receive raw cross-tenant access. Platform SREs receive masked views only. PostgreSQL does not implement “deny” in the SQL Server sense, so explicit denial is achieved here by `REVOKE ALL`, zero grants on base tables, role separation, forced RLS, and masked views only for platform operations.

**`postgres-partitioning-and-rls.sql`**
```sql
create extension if not exists pgcrypto;

create schema if not exists authz;
create schema if not exists fact;
create schema if not exists secure;

create or replace function authz.current_tenant_id()
returns text language sql stable as $$
  select nullif(current_setting('app.tenant_id', true), '')
$$;

create or replace function authz.current_role_name()
returns text language sql stable as $$
  select nullif(current_setting('app.role_name', true), '')
$$;

create or replace function authz.current_site_scope()
returns text[] language sql stable as $$
  select coalesce(string_to_array(nullif(current_setting('app.site_scope', true), ''), ','), array[]::text[])
$$;

create table fact.fact_time_event (
  tenant_id text not null,
  business_date date not null,
  time_event_id uuid not null default gen_random_uuid(),
  employee_id text not null,
  assignment_id text,
  site_id text not null,
  cost_center_id text,
  source_system text not null,
  event_kind text not null,
  occurred_at timestamptz not null,
  received_at timestamptz not null,
  payload jsonb not null,
  payload_sha256 text not null,
  decision_passport_id text,
  invariant_bundle_hash text not null,
  created_at timestamptz not null default now(),
  primary key (tenant_id, business_date, time_event_id)
) partition by list (tenant_id);

create table fact.fact_time_event_delta
  partition of fact.fact_time_event
  for values in ('delta')
  partition by range (business_date);

create table fact.fact_time_event_ascension
  partition of fact.fact_time_event
  for values in ('ascension')
  partition by range (business_date);

create table fact.fact_time_event_mgm_lv
  partition of fact.fact_time_event
  for values in ('mgm_lv')
  partition by range (business_date);

create table fact.fact_time_event_schneider
  partition of fact.fact_time_event
  for values in ('schneider')
  partition by range (business_date);

create table fact.fact_time_event_pepsico
  partition of fact.fact_time_event
  for values in ('pepsico')
  partition by range (business_date);

create table fact.fact_time_event_delta_2024
  partition of fact.fact_time_event_delta
  for values from ('2024-01-01') to ('2025-01-01');

create table fact.fact_payroll_publication (
  tenant_id text not null,
  business_date date not null,
  publication_id uuid not null default gen_random_uuid(),
  pay_group_id text not null,
  legal_entity_id text not null,
  period_start date not null,
  period_end date not null,
  publication_seq integer not null,
  export_kind text not null,
  outbox_state text not null,
  outbox_key text not null,
  rule_bundle_hash text not null,
  decision_passport_id text not null,
  payload jsonb not null,
  transmitted_at timestamptz,
  acknowledged_at timestamptz,
  created_at timestamptz not null default now(),
  primary key (tenant_id, business_date, publication_id)
) partition by list (tenant_id);

create table fact.fact_payroll_publication_delta
  partition of fact.fact_payroll_publication
  for values in ('delta')
  partition by range (business_date);

create index on fact.fact_time_event (tenant_id, employee_id, occurred_at);
create index on fact.fact_time_event (tenant_id, site_id, business_date);
create index on fact.fact_payroll_publication (tenant_id, pay_group_id, period_end);

alter table fact.fact_time_event enable row level security;
alter table fact.fact_time_event force row level security;
alter table fact.fact_payroll_publication enable row level security;
alter table fact.fact_payroll_publication force row level security;

create policy tenant_time_event_select on fact.fact_time_event
for select
using (
  tenant_id = authz.current_tenant_id()
  and (
    cardinality(authz.current_site_scope()) = 0
    or site_id = any(authz.current_site_scope())
  )
);

create policy tenant_time_event_insert on fact.fact_time_event
for insert
with check (
  tenant_id = authz.current_tenant_id()
);

create policy tenant_payroll_select on fact.fact_payroll_publication
for select
using (
  tenant_id = authz.current_tenant_id()
);

create policy tenant_payroll_update on fact.fact_payroll_publication
for update
using (
  tenant_id = authz.current_tenant_id()
  and authz.current_role_name() in ('tenant_payroll_bot', 'tenant_assurance_service')
)
with check (
  tenant_id = authz.current_tenant_id()
);

create view secure.v_time_event_masked as
select
  tenant_id,
  business_date,
  time_event_id,
  left(employee_id, 8) || '…' as employee_id_masked,
  site_id,
  cost_center_id,
  source_system,
  event_kind,
  occurred_at,
  received_at,
  decision_passport_id,
  invariant_bundle_hash,
  payload - 'biometric_template' - 'raw_face_image' - 'personally_identifiable_data' as payload_masked
from fact.fact_time_event;

create view secure.v_payroll_publication_masked as
select
  tenant_id,
  business_date,
  publication_id,
  pay_group_id,
  legal_entity_id,
  period_start,
  period_end,
  publication_seq,
  export_kind,
  outbox_state,
  outbox_key,
  rule_bundle_hash,
  decision_passport_id,
  jsonb_build_object(
    'record_count', jsonb_array_length(coalesce(payload->'records', '[]'::jsonb)),
    'totals_only', payload->'totals'
  ) as payload_masked
from fact.fact_payroll_publication;

create role app_authenticator noinherit;
create role tenant_analyst noinherit;
create role tenant_manager noinherit;
create role tenant_payroll_bot noinherit;
create role tenant_assurance_service noinherit;
create role platform_sre_masked noinherit;
create role break_glass_security_officer noinherit;

revoke all on schema fact from public;
revoke all on all tables in schema fact from public;
revoke all on all tables in schema secure from public;

grant usage on schema secure to platform_sre_masked;
grant select on secure.v_time_event_masked to platform_sre_masked;
grant select on secure.v_payroll_publication_masked to platform_sre_masked;

grant usage on schema fact to tenant_analyst, tenant_manager, tenant_payroll_bot, tenant_assurance_service;
grant select on fact.fact_time_event to tenant_analyst, tenant_manager, tenant_assurance_service;
grant select, update on fact.fact_payroll_publication to tenant_payroll_bot, tenant_assurance_service;

-- break-glass is session-gated and audited externally.
```

Minimal durable RBAC roles:

| role | permitted scope | explicit denials by grant model |
|---|---|---|
| `tenant_analyst` | same-tenant read only, optionally site-scoped | no raw biometric, no cross-tenant, no write, no invariant edits |
| `tenant_manager` | same-tenant operational read plus decision-review views | no payroll publish, no cross-tenant, no frozen invariant change |
| `tenant_payroll_bot` | same-tenant payroll outbox update path only | no tenant-wide raw reads beyond payroll-prep set, no invariant edits |
| `tenant_assurance_service` | same-tenant evidence/passport/reconciliation service ops | no cross-tenant, no direct break-glass |
| `platform_sre_masked` | masked ops views only | no base-table read, no raw biometric, no payroll payload detail |
| `break_glass_security_officer` | audited temporary elevation only | no standing access; ticket + reason + expiry mandatory |

**Integration surface**

The operational integration contract is event-first with deterministic reconciliation fallback.

**Canonical inbound envelope**
```json
{
  "schema_version": "1.0.0",
  "tenant_id": "delta",
  "source_system": "ukg_webhooks",
  "channel": "webhook",
  "event_id": "ukg-evt-12345",
  "event_type": "wfm.time.punch.changed",
  "occurred_at": "2024-07-19T12:14:33Z",
  "received_at": "2024-07-19T12:14:35Z",
  "signature": {
    "alg": "HMAC-SHA256",
    "verified": true
  },
  "replay": {
    "is_replay": false,
    "replay_of": null
  },
  "subject_keys": {
    "employee_id": "E123",
    "timecard_id": "TC999"
  },
  "payload_sha256": "7d8f0d4b5ad0d6dd10ea9e4d53a39e3b01d39ba7ccf9f9c14a3e8eb9b8bfc3a1",
  "payload": {}
}
```

The integration pattern is:

1. **UKG Webhooks ingress** for low-latency operational changes.
2. **Webhooks Premium replay/audit** for gap fill, redelivery, and forensic event retrieval.
3. **Secondary reconciliation** through scheduled pulls and batch loads for timesheets, accruals, and payroll acknowledgments.
4. **Outbox publication** for payroll exports with signed bundle hash and idempotency guarantee.
5. **People Fabric enrichment-only** for non-authoritative context enrichment, never for legality, pay, safety, or isolation-critical source-of-record decisions.

That is aligned to what UKG publicly exposes today: Webhooks are near real time and HMAC-capable; Premium supports replay/retry/audit and event retrieval; the Developer Console manages machine credentials and access rights; and WIH is a monitor, not a transactional source of truth. citeturn2search4turn2search2turn2search11turn2search3turn2search0

**UKG Webhooks + secondary reconciliation + Premium replay contract**

```yaml
webhook_ingress:
  verify_hmac: true
  dedupe_key: "{tenant_id}:{event_id}"
  accept_clock_skew_seconds: 300
  quarantine_on:
    - invalid_signature
    - duplicate_with_payload_mismatch
    - tenant_route_mismatch
    - schema_version_unknown

premium_replay:
  enabled: true
  use_cases:
    - missing_event_gap_fill
    - incident_forensics
    - delayed_delivery_recovery
  replay_controls:
    require_decision_passport: true
    write_replay_marker: true
    no_silent_overwrite: true

secondary_reconciliation:
  cadence:
    timecards: "15m during active payroll windows, hourly otherwise"
    accruals: "hourly"
    payroll_ack: "per publication cycle"
  outputs:
    - evidence_envelope
    - decision_passport_update
    - outbox_delta_batch_if_needed
```

**Payroll export outbox state machine and idempotency key formula**

The outbox is its own causal plane. No export leaves the system without a bound rule bundle, a Decision Passport, and an idempotency key.

```yaml
outbox_state_machine:
  states:
    - prepared
    - validated
    - signed
    - queued
    - transmitted
    - acknowledged
    - applied
    - corrected
    - superseded
    - quarantined
    - failed_terminal
  transitions:
    prepared_to_validated: "all invariant checks pass and worker_harm critical count = 0"
    validated_to_signed: "bundle hash and payload hash minted"
    signed_to_queued: "transport slot assigned"
    queued_to_transmitted: "delivery attempt begins"
    transmitted_to_acknowledged: "receiver confirms receipt"
    acknowledged_to_applied: "receiver posts accepted publication"
    any_to_quarantined: "evidence corruption, tenant mismatch, or unapproved replay"
    applied_to_corrected: "delta batch issued with linked prior outbox key"
```

Idempotency key formula:
```text
outbox_key = SHA256(
  tenant_id || '|' ||
  legal_entity_id || '|' ||
  pay_group_id || '|' ||
  period_start || '|' ||
  period_end || '|' ||
  publication_seq || '|' ||
  export_kind || '|' ||
  rule_bundle_hash || '|' ||
  decision_passport_id
)
```

Corrective-delta rule:
```yaml
corrective_delta_batch:
  required_fields:
    - prior_outbox_key
    - correction_reason_code
    - delta_only_payload
    - decision_passport_id
    - rule_bundle_hash
  restrictions:
    - no destructive resend of prior accepted batch
    - no merge across pay groups
    - must preserve causal pointer to original publication
```

## Generation threating and observability

**Deterministic history generator contract**

The generator does not “fake data.” It synthesizes **causal history**. It starts from scenario windows, labor geometry, policy packs, and seed hierarchy. It then injects non-uniform noise whose parameters are explicit, reproducible, and testable.

**`generate_history.py` CLI surface**
```text
python generate_history.py
  --tenant {delta|ascension|mgm_lv|schneider|pepsico}
  --start-year 2016
  --end-year 2026
  --tenant-manifest ./tenants/<tenant>.yaml
  --scenario-calendar ./control-plane/scenario-calendar.yaml
  --frozen-invariants ./control-plane/frozen-invariants.yaml
  --jurisdiction-pack ./packs/<pack>.yaml [repeatable]
  --root-seed 20260721
  --seed-salt "ukg-assurance-final"
  --noise-pack {default|conservative|stress|cyber|peak-season}
  --site-count <int>
  --employee-count <int>
  --output-dir ./out/<tenant>
  --render-signatures true
  --emit-csv true
  --emit-parquet true
  --emit-jsonl true
  --validate-only false
  --acceptance-profile strict
  --reject-on-gate-fail true
```

Parameter groups:
```yaml
parameter_groups:
  topology:
    - site_count
    - department_mix
    - role_mix
    - union_coverage_rate
  scheduling:
    - shift_templates
    - bid_line_templates
    - on_call_templates
    - seasonal_curve_pack
  payroll:
    - pay_code_distribution_pack
    - overtime_rule_pack
    - differential_pack
    - gratuity_pack
  events:
    - scenario_calendar
    - extreme_weather_pack
    - cyber_downtime_pack
    - regulatory_change_pack
  privacy_and_identity:
    - biometric_opt_out_rate
    - false_non_match_curve
    - consent_refresh_schedule
```

Seed hierarchy formula:
```text
root = BLAKE2b_256(str(root_seed) || '|' || seed_salt)

tenant_seed      = BLAKE2b_256(root || '|tenant|' || tenant_id)
year_seed        = BLAKE2b_256(tenant_seed || '|year|' || year)
site_seed        = BLAKE2b_256(year_seed || '|site|' || site_id)
employee_seed    = BLAKE2b_256(site_seed || '|employee|' || employee_id)
stream_seed      = BLAKE2b_256(employee_seed || '|stream|' || stream_name)
scenario_seed    = BLAKE2b_256(stream_seed || '|scenario|' || scenario_window_id)
noise_seed       = BLAKE2b_256(scenario_seed || '|noise|' || noise_model_name)
```

Named noise model:
```yaml
noise_models:
  hawkes_clustering:
    purpose: "self-exciting bursts for incidents, manual edits, callouts, outage queues"
    params: [mu, alpha, beta]
  markov_attendance:
    purpose: "attendance state transitions"
    states: [present, late, absent, swapped, overtime, downtime_manual]
  threshold_heaping:
    purpose: "human-biased rounding and manager tendency around thresholds"
    params: [heap_points_minutes, probability_mass]
  manager_fingerprint:
    purpose: "manager-specific approval/attestation behavior"
    params: [strictness, delay_bias, correction_bias]
  scenario_covariance:
    purpose: "co-movement among overtime, exceptions, retro-pay, and manual capture during scenario windows"
    params: [correlation_matrix_id]
```

Acceptance gates are hard rejects, not warnings:

```yaml
acceptance_gates:
  - gate: no_uniform_random_footprint
    assert: "ks_test_vs_uniform_p < 0.001 for punch timestamps in active shifts"
  - gate: public_event_window_signature_match
    assert: "known windows must produce declared directional signatures"
  - gate: tenant_invariant_respect
    assert: "no frozen invariant may be violated by generated primary facts"
  - gate: manual_recovery_presence_after_known_cyber_events
    assert: "manual_entry_share spike present for Ascension 2024-05-08+, MGM 2023-09-11+, Delta 2024-07-19..24"
  - gate: consent_alternative_path_for_biometrics
    assert: "PepsiCo years with biometric enablement include non-zero alternative path traffic in covered jurisdictions"
  - gate: cross_tenant_isolation_test
    assert: "generated IDs and hashes cannot collide in routed partitions at greater than configured collision_floor"
```

**Worked example: Delta CrowdStrike scenario calendar and generated signature**

```yaml
example_window:
  tenant_id: delta
  window_id: delta_2024_crowdstrike
  start: "2024-07-19"
  end: "2024-07-24"
  cause: "CrowdStrike-caused operational disruption and manual crew support"
  intensity:
    manual_capture_spike: 5
    legality_hold_queue: 5
    payroll_delta_batch: 4
  expected_signature:
    baseline:
      manual_crew_assignment_share: 0.06
      legality_hold_queue_per_1000_pairings: 8
      retro_pay_delta_batches_per_day: 2
    generated:
      2024-07-19:
        manual_crew_assignment_share: 0.22
        legality_hold_queue_per_1000_pairings: 31
        retro_pay_delta_batches_per_day: 4
      2024-07-20:
        manual_crew_assignment_share: 0.29
        legality_hold_queue_per_1000_pairings: 39
        retro_pay_delta_batches_per_day: 5
      2024-07-21:
        manual_crew_assignment_share: 0.33
        legality_hold_queue_per_1000_pairings: 42
        retro_pay_delta_batches_per_day: 6
      2024-07-22:
        manual_crew_assignment_share: 0.27
        legality_hold_queue_per_1000_pairings: 34
        retro_pay_delta_batches_per_day: 5
      2024-07-23:
        manual_crew_assignment_share: 0.18
        legality_hold_queue_per_1000_pairings: 21
        retro_pay_delta_batches_per_day: 3
      2024-07-24:
        manual_crew_assignment_share: 0.10
        legality_hold_queue_per_1000_pairings: 11
        retro_pay_delta_batches_per_day: 2
    generated_signature_hash: "3dfdbb8fb427b3791d9e78ce8b7a8143d9404b9199a77331ca4f46d5e297146d"
```

That example is grounded in Delta’s own public description of a July 19 schedule pause, manual repair of Windows-based systems, specific crew-tracking complexity, and return toward normal operations by July 24. citeturn5search3turn5search0turn5search5

**Threat model**

The threat model combines STRIDE with evidence-corruption modes. Every major surface gets mapped to both attack families and mandatory containment behavior.

| surface | STRIDE focus | evidence-corruption mode | detection | mandatory response |
|---|---|---|---|---|
| webhook ingress | spoofing, tampering, replay, repudiation | filtering, construction | HMAC fail, duplicate key mismatch, unexpected source route, replay without marker | quarantine envelope, open incident, no downstream write |
| manual downtime capture | tampering, repudiation, elevation of privilege | construction, performance | attestation gap, shift-shell mismatch, supervisor-only cluster, threshold-heaping anomaly | dual-key attestation, provisional-presence wage protection, delta-only publication |
| synthetic generator | tampering, information disclosure | construction, entanglement | signature mismatch to scenario calendar, impossible invariant pass-through, isotope seed mismatch | hard reject tenant-year, no artifact emission |
| payroll outbox | tampering, replay, repudiation | filtering, performance | outbox key collision, bundle-hash drift, ack without prior transmit | quarantine publication, block automation |
| invariant engine | tampering, elevation of privilege | entanglement, filtering | frozen bundle hash change, rule source downgrade, missing held-out regression | block activation, ledger incident |
| cross-tenant analytics | information disclosure, elevation of privilege | entanglement | tenant_id mismatch, masked-view bypass attempt, route-scope failure | terminate session, alert security, rotate token |

The evidence-corruption modes are defined as follows. **Filtering** means dropping or hiding disconfirming evidence. **Entanglement** means the system validates itself with insufficiently independent sources. **Construction** means invented, backfilled, or over-cleaned evidence. **Performance** means the system behaves differently under outage, pressure, or manual mode than under nominal mode. The transcript corpus explicitly warns about circular confirmation, verification trapped inside the same blind dimension, and the need for independent anchors plus writer/evaluator separation. fileciteturn0file0L63-L90 fileciteturn0file0L351-L376 fileciteturn0file0L2741-L2747

**Observability and Assurance Score**

The architecture publishes three operator dashboards and one composite score.

Dashboard set:
```yaml
dashboards:
  - payroll_integrity_command_center
  - incident_command_board
  - assurance_scorecard
```

Required metrics:
```yaml
metrics:
  - decision_passport_completeness_pct
  - anchor_integrity_avg
  - frozen_invariant_fail_rate
  - cross_tenant_isolation_fail_count
  - manual_capture_share
  - provisional_presence_open_count
  - downtime_correction_first_pass_accuracy
  - outbox_quarantine_rate
  - replay_gap_fill_latency_minutes
  - legality_breach_prevented_count
  - worker_harm_critical_open_count
```

Assurance Score formula:
```text
AssuranceScore =
  0.25 * PassportCompleteness
+ 0.20 * AnchorIntegrityAverage
+ 0.15 * (100 - FrozenInvariantViolationRateNormalized)
+ 0.10 * CrossTenantIsolationScore
+ 0.10 * DowntimeRecoveryAccuracy
+ 0.10 * PayrollOutboxIntegrity
+ 0.10 * HarmAndLegalityResponse
```

Hard gates:
```yaml
hard_gates:
  - if assurance_score < 70: "block tenant expansion"
  - if assurance_score < 50: "block payroll automation"
  - if cross_tenant_isolation_fail_count > 0: "block all releases"
  - if frozen_invariant_fail_rate > 0 on primary_verified pay/safety rules: "block publication"
  - if worker_harm_critical_open_count > 0 and unresolved: "block publication"
```

## Governance build and commercialization

**Constitutional change process for frozen invariants**

Frozen invariants are constitutional, not configurable. A change to the frozen set is valid only if it passes this chain:

```yaml
change_process:
  - proposal
  - source_proof
  - dual_control
  - held_out_regression
  - ledger_entry
  - delayed_activation
  - rollback_package
```

Operational rules:
```yaml
constitutional_rules:
  proposal:
    requires:
      - artifact_diff
      - invariant_rationale
      - impacted_tenants
  source_proof:
    requires:
      - primary_verified_source_only
      - effective_date
      - access_date
  dual_control:
    requires:
      - domain_owner_approval
      - platform_owner_approval
  held_out_regression:
    requires:
      - passed
      - no score regression on protected suites
  ledger_entry:
    requires:
      - signed_change_id
      - immutable_hash
  delayed_activation:
    default_wait_hours: 168
    emergency_legal_hotfix_wait_hours: 4
  rollback_package:
    requires:
      - prior_bundle_hash
      - restore_runbook
```

This process operationalizes two transcript rules directly: the frozen set must remain behind glass, and architecture development is not the same thing as adaptation inside the current loop. fileciteturn0file0L91-L117 fileciteturn0file0L7735-L7742

**Build pipeline**

**`build-assurance-architecture.yml`**
```yaml
name: build-assurance-architecture

on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - uses: actions/setup-node@v4
        with:
          node-version: "22"

      - name: Install toolchain
        run: |
          python -m pip install --upgrade pip
          pip install pyyaml jsonschema check-jsonschema yamllint pytest pandas scipy sqlfluff
          npm install -g ajv-cli @mermaid-js/mermaid-cli

      - name: Lint YAML
        run: yamllint control-plane tenants packs .github/workflows/build-assurance-architecture.yml

      - name: Validate JSON Schemas
        run: |
          check-jsonschema control-plane/decision-passport.schema.json
          check-jsonschema control-plane/evidence-envelope.schema.json
          check-jsonschema control-plane/autonomy-envelope.schema.json
          check-jsonschema control-plane/architecture-evolution-ledger.schema.json

      - name: Validate YAML artifacts against schemas
        run: |
          python scripts/validate_yaml_artifacts.py \
            --scenario-calendar control-plane/scenario-calendar.yaml \
            --worker-harm control-plane/worker-harm-signal-catalog.yaml \
            --frozen-invariants control-plane/frozen-invariants.yaml \
            --tenant-manifests tenants/*.yaml

      - name: Compile invariant bundles
        run: |
          python scripts/compile_invariant_bundles.py \
            --sources control-plane/frozen-invariants.yaml \
            --out build/invariants

      - name: Lint SQL and RLS
        run: sqlfluff lint sql/postgres-partitioning-and-rls.sql --dialect postgres

      - name: Render Mermaid
        run: |
          mkdir -p build/diagrams
          mmdc -i diagrams/platform.mmd -o build/diagrams/platform.svg
          mmdc -i diagrams/generator-flow.mmd -o build/diagrams/generator-flow.svg

      - name: Run schema and acceptance tests
        run: |
          pytest -q tests/control_plane
          pytest -q tests/generator_acceptance
          pytest -q tests/rls_isolation
          pytest -q tests/evidence_corruption

      - name: Package artifacts
        run: |
          mkdir -p dist
          tar -czf dist/ukg-assurance-architecture-${GITHUB_SHA}.tar.gz \
            control-plane tenants packs sql diagrams build

      - name: Upload versioned artifact package
        uses: actions/upload-artifact@v4
        with:
          name: ukg-assurance-architecture-${{ github.sha }}
          path: dist/ukg-assurance-architecture-${{ github.sha }}.tar.gz
```

**Commercial wedge sequence and KPI targets**

The commercial sequence is narrow on purpose.

| wedge | packaging | entry criteria | 90-day target | 180-day target |
|---|---|---|---|---|
| payroll-integrity investigation | design-partner service | tenant has current Webhooks or equivalent event export and one payroll team sponsor | median payroll-integrity investigation time from 4 hours baseline to **≤ 60 minutes** | **≤ 20 minutes**, with ≥ 90% of cases backed by complete Decision Passports |
| downtime correction accuracy | Marketplace or managed add-on | tenant has manual downtime history or high-risk operational exposure | first-pass downtime correction accuracy from 88% baseline to **≥ 97%** | **≥ 99.5%**, with provisional-presence wage protection on 100% of uncertainty cases |
| HOS and legality breach prevention | OEM / regulated assurance module | regulated scheduling environment and source legality data available | prevented or blocked legality breaches reduce escaped events from 3.0 per 10k regulated duties to **≤ 1.0 per 10k** | **≤ 0.3 per 10k**, with 100% of override attempts passported and dual-approved |

Baseline assumptions:
```yaml
baseline_assumptions:
  payroll_integrity_investigation_time_median_minutes: 240
  downtime_correction_first_pass_accuracy_pct: 88
  escaped_legality_breaches_per_10k_regulated_duties: 3.0
```

Packaging sequence:
```yaml
commercial_sequence:
  - phase: design_partner
    success_gate: "repeatable 90-day KPI win in one tenant"
  - phase: marketplace_add_on
    success_gate: "installation and manifest compilation repeatable without bespoke engineering"
  - phase: oem_module
    success_gate: "RLS, outbox, and generator acceptance packs standardized"
  - phase: acquisition_option
    success_gate: "assurance layer becomes prerequisite for UKG-controlled agentic WFM workflows"
```

**Final non-negotiables**

Any rule that can affect payroll, legality, safety, or cross-tenant access must exist as a **schema, signed bundle, policy, test, or ledgered change event**. Prose is insufficient.

The final non-negotiables are:

1. No payroll publication without a Decision Passport.
2. No optimizer may weaken a primary-verified frozen invariant outside the constitutional change process.
3. Writer and evaluator must remain structurally separate for consequential decisions. fileciteturn0file0L2741-L2747
4. Every consequential decision must carry at least one independent anchor and an anchor-integrity score. fileciteturn0file0L82-L89
5. Human domain owners originate the root value hierarchy and approve frozen-invariant changes. fileciteturn0file0L98-L104
6. People Fabric remains enrichment-only until tenant certification proves exact-workload stability on this platform surface. citeturn3search0
7. Any biometric attendance flow must have an alternative non-biometric path where required, plus manual review and no worker detriment on automated failure. citeturn16search0turn16search2
8. Any known public disruption window that should create a signal spike must do so in synthetic history or the tenant-year is rejected. citeturn5search3turn5search5turn6search3turn5search1
9. Cross-tenant reads from analyst, manager, bot, or agent surfaces are prohibited by structure, not by convention.
10. Break-glass access is temporary, masked where possible, ticketed, reason-coded, and externally auditable.
11. Containment beats command: autonomy envelopes define what must remain true, not free-form override power. fileciteturn0file0L1518-L1531 fileciteturn0file0L7724-L7729
12. Pain channels are first-class. Anything that risks lost wages, unsafe work, legality breach, or tenant leakage bypasses dashboard smoothing and opens the algadonic path immediately. fileciteturn0file0L8064-L8076

This markdown constitution is therefore the single source of truth for later code generation of P01 through P05 under the five locked tenant overlays.