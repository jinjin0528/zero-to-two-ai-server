from infrastructure.llm.client import client
from infrastructure.llm.prompts.agent2.agent2_prompt import (
    TENANT_RECOMMEND_REASON_SYSTEM,
    TENANT_RECOMMEND_REASON_USER_TEMPLATE,
)
from infrastructure.llm.schemas.agent2_schema import (
    TenantRecommendReasonInput,
    TenantRecommendReasonOutput,
)


async def generate_tenant_recommend_reason(
    data: TenantRecommendReasonInput,
) -> TenantRecommendReasonOutput:
    user_prompt = TENANT_RECOMMEND_REASON_USER_TEMPLATE.format(
        tenant_summary=data.tenant_summary,
        property_info=data.property_info,
    )

    json_resp = await llm_client.generate_json(
        system_prompt=TENANT_RECOMMEND_REASON_SYSTEM,
        user_prompt=user_prompt,
    )

    return TenantRecommendReasonOutput(**json_resp)