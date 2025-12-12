import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app import main
import app.api.routes.tenant as llm_route
from infrastructure.llm.clients import openai_client


def test_ai_test_endpoint(monkeypatch):
    monkeypatch.setattr(llm_route, "ask_llm", lambda prompt: "mocked-response")

    client = TestClient(main.app)
    response = client.post("/ai/tests", json={"prompt": "안녕"})

    assert response.status_code == 200
    assert response.json() == {"response": "mocked-response"}


def test_agent1_clean_requirement(monkeypatch):
    async def fake_generate_json(system_prompt: str, user_prompt: str):
        return {"clean_summary": "정제된 문장"}

    monkeypatch.setattr(openai_client.llm_client, "generate_json", fake_generate_json)

    client = TestClient(main.app)
    response = client.post(
        "/agent1/tenant/clean", json={"tenant_raw_input": "마포구 신축"}
    )

    assert response.status_code == 200
    assert response.json() == {"clean_summary": "정제된 문장"}


def test_agent1_property_description(monkeypatch):
    calls = {}

    async def fake_generate_json(system_prompt: str, user_prompt: str):
        calls["system"] = system_prompt
        calls["user"] = user_prompt
        return {"description": "깔끔한 매물 소개"}

    monkeypatch.setattr(openai_client.llm_client, "generate_json", fake_generate_json)

    client = TestClient(main.app)
    response = client.post(
        "/agent1/property/description",
        json={"property_raw_input": "역세권 오피스텔"},
    )

    assert response.status_code == 200
    assert response.json() == {"description": "깔끔한 매물 소개"}
    assert "역세권 오피스텔" in calls["user"]


def test_agent2_recommend_reason(monkeypatch):
    async def fake_generate_json(system_prompt: str, user_prompt: str):
        return {"reason": "역세권이라 적합"}

    monkeypatch.setattr(openai_client.llm_client, "generate_json", fake_generate_json)

    client = TestClient(main.app)
    response = client.post(
        "/agent2/recommend/reason",
        json={
            "tenant_summary": "마포구 선호",
            "property_info": "마포역 도보 1분 전세",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"reason": "역세권이라 적합"}


def test_agent3_recommend_reason(monkeypatch):
    async def fake_generate_json(system_prompt: str, user_prompt: str):
        return {"reason": "예산과 조건이 잘 맞음"}

    monkeypatch.setattr(openai_client.llm_client, "generate_json", fake_generate_json)

    client = TestClient(main.app)
    response = client.post(
        "/agent3/recommend/reason",
        json={
            "property_info": "용산구 오피스텔",
            "tenant_summary": "용산 직장인 월세 선호",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"reason": "예산과 조건이 잘 맞음"}