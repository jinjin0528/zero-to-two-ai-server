from textwrap import dedent
from typing import List, Optional


def build_requirement_summary_prompt(requirements: List[str], must_have: Optional[List[str]] = None) -> str:
    must_have = must_have or []
    user_lines = "\n".join(f"- {item}" for item in requirements)
    must_lines = "\n".join(f"- {item}" for item in must_have) if must_have else "- (없음)"

    return dedent(
        f"""
        너는 부동산 임차인 요구사항을 요약·정제하는 에이전트다.
        - 중복/모호한 표현은 통합하고, 가격·지역·평형·구조·옵션을 명확히 정리한다.
        - 개인정보나 연락처는 절대 포함하지 말고 제거한 이유를 설명한다.
        - 아래 JSON 스키마를 정확히 따르라.

        [요구조건 목록]
        {user_lines}

        [절대 빠뜨리지 말아야 할 필수 조건]
        {must_lines}

        [반환 JSON 스키마]
        {{
          "must_conditions": ["문자열"],
          "nice_to_have": ["문자열"],
          "removed_items": ["삭제한 항목에 대한 설명"],
          "style": "요약 톤 가이드 (예: 친절하고 간결하게)"
        }}
        """
    ).strip()


def build_listing_description_prompt(listing_facts: List[str], tone: str = "친절하고 신뢰감 있게") -> str:
    facts = "\n".join(f"- {fact}" for fact in listing_facts)
    return dedent(
        f"""
        너는 임대인 매물 설명을 작성하는 에이전트다.
        - 과장하지 말고 사실 기반으로만 작성한다.
        - 한국 부동산 용어를 사용하고, 층/면적/가격 단위를 명확히 표기한다.
        - 연락처나 개인정보는 포함하지 않는다.

        [매물 팩트]
        {facts}

        [요청 톤]
        {tone}

        [반환 JSON 스키마]
        {{
          "headline": "한 줄 매물 소개",
          "highlights": ["특징 3~5개"],
          "full_text": "상세 설명 2~3문단",
          "caveats": ["주의사항 또는 누락된 정보"]
        }}
        """
    ).strip()