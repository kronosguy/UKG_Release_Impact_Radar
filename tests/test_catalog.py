import yaml
from generator.config import REPO_ROOT


def test_catalog_has_337_objects():
    catalog = yaml.safe_load((REPO_ROOT / "config/export-object-catalog.yaml").read_text(encoding="utf-8"))
    assert len(catalog["spec"]["objects"]) == 337
