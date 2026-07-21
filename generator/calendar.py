from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any


@dataclass(frozen=True)
class ActiveScenario:
    scenario_id: str
    cause: str
    effects: dict[str, float]
    expected: dict[str, float]


def active_scenarios(calendar: dict[str, Any], tenant_key: str, day: date) -> list[ActiveScenario]:
    result: list[ActiveScenario] = []
    for raw in calendar.get("overlays", {}).get(tenant_key, []):
        start = date.fromisoformat(raw["start"])
        end = date.fromisoformat(raw["end"])
        if start <= day <= end:
            result.append(ActiveScenario(
                scenario_id=raw["id"],
                cause=raw["cause"],
                effects={key: float(value) for key, value in raw.get("effects", {}).items()},
                expected={key: float(value) for key, value in raw.get("expected", {}).items()},
            ))
    return result


def combined_effect(scenarios: list[ActiveScenario], key: str, default: float = 1.0) -> float:
    value = default
    for scenario in scenarios:
        if key in scenario.effects:
            if key == "operation_volume":
                value *= scenario.effects[key]
            else:
                value *= scenario.effects[key]
    return value
