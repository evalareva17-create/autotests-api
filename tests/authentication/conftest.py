"""
Локальный conftest.py для модуля authentication
Фикстуры доступны ТОЛЬКО в tests/authentication/ и подкаталогах
"""
import pytest
from clients.authentication.authentication_client import get_authentication_client


@pytest.fixture
def auth_client():
    """
    Локальная фикстура для authentication модуля
    Доступна только в тестах внутри tests/authentication/
    """
    return get_authentication_client()


@pytest.fixture
def auth_headers():
    """Фикстура с заголовками для аутентификации"""
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
