"""Pytest fixtures for tests."""

import pytest

from api.contacts import ContactsApi
from api.companies import CompaniesApi
from api.deals import DealsApi
from api.users import UsersApi
from core.http_client import HTTPClient


@pytest.fixture
def http_client():
    """HTTP client fixture."""
    client = HTTPClient()
    yield client
    client.close()


@pytest.fixture
def contacts_api(http_client):
    """Contacts API fixture."""
    return ContactsApi(http_client)


@pytest.fixture
def companies_api(http_client):
    """Companies API fixture."""
    return CompaniesApi(http_client)


@pytest.fixture
def deals_api(http_client):
    """Deals API fixture."""
    return DealsApi(http_client)


@pytest.fixture
def users_api(http_client):
    """Users API fixture."""
    return UsersApi(http_client)


@pytest.fixture
def sample_contact():
    return {"name": "Test User", "email": "test@example.com", "phone": "+1234567890"}


@pytest.fixture
def sample_company():
    return {"name": "Test Company", "website": "https://test.com", "phone": "+1234567890"}


@pytest.fixture
def sample_deal():
    return {"name": "Test Deal", "price": 10000}
