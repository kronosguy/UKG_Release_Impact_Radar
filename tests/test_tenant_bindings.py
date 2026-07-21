from generator.config import load_tenant


def test_locked_bindings():
    assert load_tenant("mgm_lv").primary_project == "P01"
    assert load_tenant("ascension").primary_project == "P02"
    assert load_tenant("delta").primary_project == "P03"
    assert load_tenant("schneider").primary_project == "P04"
    assert load_tenant("pepsico").primary_project == "P05"


def test_mgm_dual_identifier_resolution():
    config = load_tenant("mgm_lv")
    assert config.package_slug == "mgm"
    assert config.tenant_key == "mgm_lv"
