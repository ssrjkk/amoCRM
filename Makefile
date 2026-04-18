.PHONY: help test-api test-ui test-db test-kafka test-load test-all test smoke install infra-clean infra-up infra-down

help:
	@echo " Доступные команды:"
	@echo "  make install          - Установить зависимости"
	@echo "  make test-api         - Запустить API тесты"
	@echo "  make test-ui         - Запустить UI тесты"
	@echo "  make test-db          - Запустить DB тесты"
	@echo "  make test-kafka       - Запустить Kafka тесты"
	@echo "  make test-load       - Запустить нагрузочные тесты"
	@echo "  make test-all        - Запустить все тесты"
	@echo "  make smoke           - Запустить smoke тесты"
	@echo "  make infra-up        - Поднять инфраструктуру"
	@echo "  make infra-down      - Остановить инфраструктуру"

# Install
install:
	pip install -e ".[all]"

# API tests
test-api:
	pytest src/api/ -m api -v -n auto --alluredir=reports/allure-api

# UI tests
test-ui:
	pytest src/ui/ -m ui -v -n auto --alluredir=reports/allure-ui

# DB tests
test-db:
	pytest src/db/ -m db -v -n auto --alluredir=reports/allure-db

# Kafka tests
test-kafka:
	pytest src/kafka/ -m kafka -v -n auto --alluredir=reports/allure-kafka

# Load tests
test-load:
	locust -f src/load/locustfile.py --headless --users 50 --run-time 60s

# All tests
test-all:
	pytest src/ -v -n auto --alluredir=reports/allure

# Smoke tests
smoke:
	pytest src/ -m smoke -v

# Infrastructure
infra-up:
	docker-compose -f infra/docker-compose.yml --profile all up -d

infra-down:
	docker-compose -f infra/docker-compose.yml --profile all down

infra-clean:
	docker-compose -f infra/docker-compose.yml --profile all down -v