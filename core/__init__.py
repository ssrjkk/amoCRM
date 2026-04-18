"""Core module - базовые компоненты для всех пайплайнов."""
from .config import Settings, get_settings
from .logger import get_logger
from .fixtures import *
from .allure import attach_screenshot, attach_log

__all__ = [
    "Settings",
    "get_settings", 
    "get_logger",
    "attach_screenshot", 
    "attach_log",
]