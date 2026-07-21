import json
from pathlib import Path

from generator.sdm import build_sdm_export
from generator.config import REPO_ROOT


def test_sdm_responses_remain_empty(tmp_path: Path):
    assert build_sdm_export(REPO_ROOT, tmp_path, "delta", "Delta Air Lines", "delta") == 337
    files = list((tmp_path / "sdm-export").glob("*/response.json"))
    assert len(files) == 337
    for path in files:
        payload = json.loads(path.read_text(encoding="utf-8"))
        assert payload["itemsRetrieveResponseDTOs"] == []
        assert payload["itemsRetrieveResponses"] == []
