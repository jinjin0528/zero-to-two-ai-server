import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from infrastructure.llm.prompts.agent1_prompt import (
    PROPERTY_DESCRIPTION_USER_TEMPLATE,
    TENANT_REQUIREMENT_USER_TEMPLATE,
)
from infrastructure.llm.prompts.agent2_prompt import (
    TENANT_RECOMMEND_REASON_USER_TEMPLATE,
)
from infrastructure.llm.prompts.agent3_prompt import (
    LANDLORD_RECOMMEND_REASON_USER_TEMPLATE,
)


def test_agent1_requirement_prompt_contains_placeholder():
    prompt = TENANT_REQUIREMENT_USER_TEMPLATE.format(tenant_raw_input="역세권 원해요")

    assert "역세권 원해요" in prompt
    assert "clean_summary" in prompt


def test_agent1_listing_description_prompt_contains_placeholder():
    prompt = PROPERTY_DESCRIPTION_USER_TEMPLATE.format(property_raw_input="마포역 도보")

    assert "마포역 도보" in prompt
    assert "description" in prompt


def test_agent2_prompt_contains_tenant_and_property_context():
    prompt = TENANT_RECOMMEND_REASON_USER_TEMPLATE.format(
        tenant_summary="마포구 신축 선호",
        property_info="마포역 초역세권 전세 5억",
    )

    assert "마포구 신축 선호" in prompt
    assert "마포역 초역세권 전세 5억" in prompt
    assert "reason" in prompt


def test_agent3_prompt_contains_property_and_tenant_context():
    prompt = LANDLORD_RECOMMEND_REASON_USER_TEMPLATE.format(
        property_info="용산역 도보 3분",
        tenant_summary="용산 직장인 월세 선호",
    )

    assert "용산역 도보 3분" in prompt
    assert "용산 직장인 월세 선호" in prompt
    assert "reason" in prompt