"""
Локальный conftest.py для модуля users
Фикстуры доступны ТОЛЬКО в tests/users/ и подкаталогах
"""
import pytest
from clients.users.public_users_client import get_public_users_client


@pytest.fixture
def users_api_client():
    """
    Локальная фикстура для users модуля
    Доступна только в тестах внутри tests/users/
    """
    client = get_public_users_client()
    yield client
    # Teardown: можно добавить очистку


@pytest.fixture
def user_roles():
    """Фикстура с ролями пользователей для тестов"""
    return ["admin", "user", "guest"]
