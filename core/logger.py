"""Общий логгер с JSON-форматом для парсинга в Kibana."""
import logging
import sys
import json
from datetime import datetime
from typing import Any
from functools import lru_cache

from core.config import get_settings


class JSONFormatter(logging.Formatter):
    """Форматтер для JSON-логов (парсинг в Kibana)."""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        if hasattr(record, "extra"):
            log_data.update(record.extra)
        
        return json.dumps(log_data)


class PlainFormatter(logging.Formatter):
    """Обычный форматтер для консоли."""
    
    def __init__(self):
        super().__init__(
            fmt="%(asctime)s | %(level)-8s | %(name)s | %(message)s",
            datefmt="%H:%M:%S"
        )


def get_logger(name: str) -> logging.Logger:
    """Получить логгер с настройками из конфига."""
    settings = get_settings()
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(getattr(logging, settings.log_level))
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(PlainFormatter())
        logger.addHandler(console_handler)
        
        # File handler (JSON)
        try:
            file_handler = logging.FileHandler("logs/test.log")
            file_handler.setFormatter(JSONFormatter())
            logger.addHandler(file_handler)
        except Exception:
            pass
    
    logger.propagate = False
    return logger


@lru_cache
def get_test_logger() -> logging.Logger:
    """Логгер для тестов."""
    return get_logger("tests")