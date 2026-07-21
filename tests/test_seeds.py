from generator.seeds import derive_hex, stable_id


def test_seed_is_deterministic():
    assert derive_hex(20260721, "delta", 2024) == derive_hex(20260721, "delta", 2024)
    assert derive_hex(20260721, "delta", 2024) != derive_hex(20260721, "ascension", 2024)


def test_ids_are_tenant_separated():
    assert stable_id("wrk", "delta", 1) != stable_id("wrk", "ascension", 1)
