"""API tests conftest."""

import pytest
from src.api.client import AmoCRMClient
from core.config import get_settings


@pytest.fixture(scope="session")
def api_client() -> AmoCRMClient:
    """API client с токеном."""
    return AmoCRMClient()


@pytest.fixture(scope="session")
def api_client_no_token() -> AmoCRMClient:
    """API client без токена."""
    return AmoCRMClient(token=None)


@pytest.fixture(scope="function")
def test_contact(api_client):
    """Создать тестовый контакт и удалить после."""
    resp = api_client.create_contact({"name": "Test Contact"})

    if resp.status_code != 200:
        yield None
    else:
        contact_id = resp.json()["_embedded"]["contacts"][0]["id"]
        yield contact_id
        try:
            api_client.delete_contact(contact_id)
        except Exception:
            pass
