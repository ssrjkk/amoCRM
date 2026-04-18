"""Базовые фикстуры для всех пайплайнов."""
import pytest
import os
import allure
from typing import Generator, Optional
from contextlib import contextmanager

from core.config import get_settings, Settings
from core.logger import get_logger


@pytest.fixture(scope="session")
def settings() -> Settings:
    """Настройки проекта."""
    return get_settings()


@pytest.fixture(scope="session")
def logger():
    """Логгер для тестов."""
    return get_logger("tests")


@pytest.fixture(scope="session")
def amocrm_api_url() -> str:
    """URL для amoCRM API."""
    return get_settings().amocrm_api_url


@pytest.fixture(scope="session")
def amocrm_token() -> Optional[str]:
    """Токен для amoCRM API."""
    return get_settings().amocrm_long_token


@contextmanager
def allure_section(name: str):
    """Секция в Allure-отчёте."""
    with allure.step(name):
        yield


@pytest.fixture(scope="function")
def test_id(request) -> str:
    """ID теста для логов."""
    return f"{request.node.module}:{request.node.name}"


@pytest.fixture(autouse=True)
def log_test_start(request, logger):
    """Логировать начало каждого теста."""
    logger.info(f"START: {request.node.name}")
    yield
    logger.info(f"END: {request.node.name}")


def pytest_configure(config):
    """Регистрация маркеров."""
    config.addinivalue_line("markers", "api: API tests")
    config.addinivalue_line("markers", "db: Database tests")
    config.addinivalue_line("markers", "kafka: Kafka tests")
    config.addinivalue_line("markers", "load: Load tests")
    config.addinivalue_line("markers", "k8s: Kubernetes tests")
    config.addinivalue_line("markers", "ui: UI tests")
    config.addinivalue_line("markers", "logs: Log analysis tests")
    config.addinivalue_line("markers", "smoke: Quick smoke tests")
    config.addinivalue_line("markers", "critical: Critical tests")


def pytest_runtest_makereport(item, call):
    """Прикрепить скриншот/логи при падении."""
    if call.excinfo is not None and call.when == "call":
        # Add screenshot/logs attachment here if needed
        pass