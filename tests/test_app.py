import asyncio

import httpx
import pytest
from asgi_lifespan import LifespanManager
from fastapi import status

from app.main import api


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def test_client():
    async with LifespanManager(api):
        async with httpx.AsyncClient(app=api, base_url="http://app.io") as test_client:
            yield test_client


@pytest.mark.asyncio
async def test_create_articles(test_client: httpx.AsyncClient):
    payload = {"title": "test", "body": "test body"}
    response = await test_client.post("/articles", json=payload)

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_read_article(test_client: httpx.AsyncClient):
    response = await test_client.get("/articles")

    assert response.status_code == status.HTTP_200_OK
