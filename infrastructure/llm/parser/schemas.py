import json
from dataclasses import dataclass, field
from typing import List, Dict, Any


class LLMParseError(ValueError):
    """LLM 응답이 기대 스키마와 맞지 않을 때 발생."""


def _require_list(payload: Dict[str, Any], key: str) -> List[str]:
    value = payload.get(key, [])
    if not isinstance(value, list):
        raise LLMParseError(f"'{key}' 필드는 리스트여야 합니다.")
    return [str(item) for item in value]


@dataclass
class RequirementSummary:
    must_conditions: List[str] = field(default_factory=list)
    nice_to_have: List[str] = field(default_factory=list)
    removed_items: List[str] = field(default_factory=list)
    style: str = "친절하고 간결하게"

    @classmethod
    def from_json(cls, raw_text: str) -> "RequirementSummary":
        try:
            data = json.loads(raw_text)
        except json.JSONDecodeError as exc:
            raise LLMParseError("JSON 파싱 실패: " + str(exc)) from exc

        must_conditions = _require_list(data, "must_conditions")
        nice_to_have = _require_list(data, "nice_to_have")
        removed_items = _require_list(data, "removed_items")
        style = str(data.get("style", "친절하고 간결하게"))

        return cls(
            must_conditions=must_conditions,
            nice_to_have=nice_to_have,
            removed_items=removed_items,
            style=style,
        )


@dataclass
class ListingDescription:
    headline: str
    highlights: List[str]
    full_text: str
    caveats: List[str]

    @classmethod
    def from_json(cls, raw_text: str) -> "ListingDescription":
        try:
            data = json.loads(raw_text)
        except json.JSONDecodeError as exc:
            raise LLMParseError("JSON 파싱 실패: " + str(exc)) from exc

        return cls(
            headline=str(data.get("headline", "")),
            highlights=_require_list(data, "highlights"),
            full_text=str(data.get("full_text", "")),
            caveats=_require_list(data, "caveats"),
        )


__all__ = [
    "LLMParseError",
    "RequirementSummary",
    "ListingDescription",
]