import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from infrastructure.llm.parser.schemas import (
    LLMParseError,
    ListingDescription,
    RequirementSummary,
)


def test_requirement_summary_parses_lists():
    raw = """
    {
        "must_conditions": ["역세권", "풀옵션"],
        "nice_to_have": ["반려동물 가능"],
        "removed_items": [],
        "style": "친절하게"
    }
    """
    summary = RequirementSummary.from_json(raw)

    assert summary.must_conditions == ["역세권", "풀옵션"]
    assert summary.nice_to_have == ["반려동물 가능"]
    assert summary.removed_items == []
    assert summary.style == "친절하게"


def test_requirement_summary_raises_on_non_list():
    raw = """
    {
        "must_conditions": "역세권",
        "nice_to_have": ["풀옵션"],
        "removed_items": []
    }
    """
    with pytest.raises(LLMParseError):
        RequirementSummary.from_json(raw)


def test_listing_description_parses_fields():
    raw = """
    {
        "headline": "마포역 도보 2분 신축 오피스텔",
        "highlights": ["채광우수", "풀옵션"],
        "full_text": "신축 오피스텔로 역세권에 위치합니다.",
        "caveats": ["반려동물 불가"]
    }
    """
    description = ListingDescription.from_json(raw)

    assert description.headline == "마포역 도보 2분 신축 오피스텔"
    assert description.highlights == ["채광우수", "풀옵션"]
    assert description.full_text.startswith("신축 오피스텔")
    assert description.caveats == ["반려동물 불가"]


def test_listing_description_raises_on_non_list():
    raw = """
    {
        "headline": "테스트",
        "highlights": "문자열",
        "full_text": "내용",
        "caveats": []
    }
    """
    with pytest.raises(LLMParseError):
        ListingDescription.from_json(raw)