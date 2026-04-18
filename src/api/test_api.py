"""API tests - примеры."""

import pytest


pytestmark = pytest.mark.api


class TestContacts:
    """Тесты контактов."""

    def test_list_contacts(self, api_client):
        """Получить список контактов."""
        resp = api_client.list_contacts()
        assert resp.status_code in [200, 401]

    def test_create_contact(self, api_client):
        """Создать контакт."""
        resp = api_client.create_contact({"name": "Test API Contact"})
        assert resp.status_code in [200, 201, 401]

    def test_list_leads(self, api_client):
        """Получить список сделок."""
        resp = api_client.list_leads()
        assert resp.status_code in [200, 401]

    def test_list_pipelines(self, api_client):
        """Получить список воронок."""
        resp = api_client.list_pipelines()
        assert resp.status_code in [200, 401]


class TestAccount:
    """Тесты аккаунта."""

    def test_account_info(self, api_client):
        """Информация об аккаунте."""
        resp = api_client.get_account()
        assert resp.status_code in [200, 401]

    def test_list_users(self, api_client):
        """Список пользователей."""
        resp = api_client.list_users()
        assert resp.status_code in [200, 401]


class TestAuth:
    """Тесты авторизации."""

    def test_no_token_401(self, api_client_no_token):
        """Без токена - 401."""
        resp = api_client_no_token.get_account()
        assert resp.status_code == 401
