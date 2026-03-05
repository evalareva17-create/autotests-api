"""
Пример теста в модуле users
Имеет доступ к:
- Глобальным фикстурам из tests/conftest.py
- Локальным фикстурам из tests/users/conftest.py
НЕ имеет доступа к фикстурам из tests/authentication/conftest.py
"""
import pytest


def test_users_with_local_fixture(users_api_client, user_roles):
    """
    Использует локальные фикстуры из tests/users/conftest.py:
    - users_api_client
    - user_roles
    """
    assert users_api_client is not None
    assert "admin" in user_roles


def test_users_with_global_fixture(user_data, public_users_client):
    """
    Использует глобальные фикстуры из tests/conftest.py:
    - user_data
    - public_users_client
    """
    assert user_data.email is not None
    assert public_users_client is not None
