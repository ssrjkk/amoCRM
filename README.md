# amoCRM QA Automation Framework

Модульный фреймворк для автоматизации тестирования amoCRM API v4.

## Структура проекта

```
amocrm-qa/
├── src/                    # Модульные пайплайны
│   ├── api/               # API тесты
│   ├── ui/               # UI тесты (Playwright)
│   ├── db/               # Database тесты
│   ├── kafka/            # Kafka тесты
│   ├── load/             # Нагрузочные тесты
│   ├── k8s/              # Kubernetes тесты
│   └── logs/             # Log analysis
├── core/                  # Общие компоненты
│   ├── config.py         # Настройки (pydantic-settings)
│   ├── logger.py        # JSON логгер
│   ├── fixtures.py       # Базовые фикстуры
│   └── allure.py         # Allure утилиты
├── utils/                 # Утилиты
│   ├── retry.py         # Retry декоратор
│   ├── wait.py         # Wait утилиты
│   └── schema.py        # Schema валидация
├── tests/                # Интеграционные тесты
├── infra/                # Docker + K8s
│   └── docker-compose.yml
├── .github/workflows/    # CI/CD
├── pyproject.toml       # Зависимости
├── Makefile             # Команды
└── README.md
```

## Быстрый старт (5 минут)

```bash
# 1. Клонировать и перейти в папку
cd amocrm-qa

# 2. Установить зависимости
pip install -e ".[all]"

# 3. Настроить токен (в .env или GitHub Secrets)
echo "AMOCRM_LONG_TOKEN=your_token" > .env
echo "AMOCRM_SUBDOMAIN=your_subdomain" >> .env

# 4. Запустить тесты
make test-api
```

## Настройка

### Переменные окружения

Создайте файл `.env`:

```env
# amoCRM (обязательно)
AMOCRM_LONG_TOKEN=your_long_token
AMOCRM_SUBDOMAIN=your_subdomain

# Database (опционально)
DATABASE_URL=postgresql://user:pass@localhost:5432/amocrm

# Kafka (опционально)
KAFKA_BROKERS=localhost:9092
```

### GitHub Secrets

- `AMOCRM_LONG_TOKEN` — долгосрочный токен
- `AMOCRM_SUBDOMAIN` — домен аккаунта
- `DATABASE_URL` — PostgreSQL
- `KAFKA_BROKERS` — Kafka
- `LOAD_TARGET_URL` — URL для нагрузки

## Запуск тестов

```bash
# Один пайплайн
make test-api
make test-ui
make test-db

# Все тесты
make test-all

# Docker инфраструктура
make infra-up
make infra-down
```

CI/CD запускается автоматически:
- При push в main/develop
- По расписанию (ежедневно)
- Вручную через workflow_dispatch

## Добавление нового пайплайна

1. Создать папку `src/<name>/`
2. Добавить `__init__.py`, `conftest.py`, тесты
3. Зарегистрировать маркер в `pyproject.toml`
4. Добавить job в `.github/workflows/test.yml`

## Приоритеты для портфолио

1. **API tests** — основные, показывают работу с REST API
2. **UI tests (Playwright)** — современный подход, POM
3. **Load tests (Locust)** — пороговая проверка
4. **DB tests** — валидация данных
5. **Kafka tests** — собы��ийный подход

## Зависимости

```toml
[project.optional-dependencies]
core = ["pydantic>=2.10", "pydantic-settings>=2.7", "tenacity>=9.0"]
api = ["requests>=2.32", "jsonschema>=4.23"]
ui = ["playwright>=1.49"]
selenium = ["selenium>=4.20"]
db = ["psycopg2-binary>=2.9"]
kafka = ["kafka-python>=2.0"]
load = ["locust>=2.29"]
k8s = ["kubernetes>=29.0"]
logs = ["elasticsearch>=8.17"]
test = ["pytest>=8.3", "pytest-xdist>=3.6", "allure-pytest>=2.13"]
```

## Требования

- Python 3.10+
- Docker (для инфраструктуры)
- Токен amoCRM API v4

## Лицензия

MIT