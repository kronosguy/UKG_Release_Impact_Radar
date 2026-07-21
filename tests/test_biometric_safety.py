from generator.config import load_tenant


def test_pepsico_requires_biometric_privacy_pack():
    config = load_tenant("pepsico")
    assert "illinois_bipa" in config.jurisdiction_packs
    assert "ico_worker_biometrics" in config.jurisdiction_packs
