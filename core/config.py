"""Конфигурация проекта через pydantic-settings."""
from functools import lru_cache
from typing import Optional, List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Базовая конфигурация проекта."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    
    # amoCRM
    amocrm_subdomain: str = Field(default="test", alias="AMOCRM_SUBDOMAIN")
    amocrm_api_base: str = Field(default="", alias="AMOCRM_API_BASE")
    amocrm_long_token: str = Field(default="", alias="AMOCRM_LONG_TOKEN")
    client_id: str = Field(default="", alias="CLIENT_ID")
    client_secret: str = Field(default="", alias="CLIENT_SECRET")
    redirect_uri: str = Field(default="http://localhost:8080/callback", alias="REDIRECT_URI")
    
    # Database
    database_url: str = Field(default="postgresql://user:pass@localhost:5432/amocrm", alias="DATABASE_URL")
    
    # Kafka
    kafka_brokers: List[str] = Field(default=["localhost:9092"], alias="KAFKA_BROKERS")
    
    # K8s
    k8s_namespace: str = Field(default="default", alias="K8S_NAMESPACE")
    
    # Kibana/Elasticsearch
    kibana_url: str = Field(default="http://localhost:5601", alias="KIBANA_URL")
    es_host: str = Field(default="http://localhost:9200", alias="ES_HOST")
    
    # Selenium
    selenium_grid: str = Field(default="http://localhost:4444/wd/hub", alias="SELENIUM_GRID")
    browsers: List[str] = Field(default=["chrome", "firefox", "edge"])
    
    # Load testing
    load_target_url: str = Field(default="http://localhost:8080", alias="LOAD_TARGET_URL")
    load_thresholds_p95_ms: int = Field(default=500, alias="LOAD_THRESHOLD_P95_MS")
    load_thresholds_error_rate_pct: float = Field(default=1.0, alias="LOAD_THRESHOLD_ERROR_RATE")
    load_thresholds_rps_min: int = Field(default=100, alias="LOAD_THRESHOLD_RPS_MIN")
    
    # Test config
    parallel_workers: str = Field(default="auto", alias="PARALLEL_WORKERS")
    allure_dir: str = Field(default="reports/allure-results", alias="ALLURE_DIR")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    
    @property
    def amocrm_api_url(self) -> str:
        """Получить Base URL для amoCRM API."""
        if self.amocrm_api_base:
            return self.amocrm_api_base
        return f"https://{self.amocrm_subdomain}.amocrm.ru/api/v4"


@lru_cache
def get_settings() -> Settings:
    """Получить экземпляр настроек (cached)."""
    return Settings()


def get_amocrm_api_url() -> str:
    """URL для amoCRM API."""
    return get_settings().amocrm_api_url


def get_amocrm_token() -> str:
    """Токен для amoCRM API."""
    return get_settings().amocrm_long_token