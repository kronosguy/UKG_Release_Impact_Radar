from generator.config import load_tenant, REPO_ROOT


def test_every_tenant_pack_exists():
    for tenant in ["mgm_lv", "ascension", "delta", "schneider", "pepsico"]:
        config = load_tenant(tenant)
        for pack in config.jurisdiction_packs:
            assert (REPO_ROOT / "packs" / f"{pack}.yaml").exists(), (tenant, pack)
