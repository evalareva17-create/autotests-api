"""
Пример теста в модуле authentication
Имеет доступ к:
- Глобальным фикстурам из tests/conftest.py
- Локальным фикстурам из tests/authentication/conftest.py
"""
import pytest


def test_auth_with_local_fixture(auth_client, auth_headers):
    """
    Использует локальные фикстуры из tests/authentication/conftest.py:
    - auth_client
    - auth_headers
    """
    assert auth_client is not None
    assert "Content-Type" in auth_headers


def test_auth_with_global_fixture(user_data):
    """
    Использует глобальную фикстуру из tests/conftest.py:
    - user_data (доступна во всех тестах)
    """
    assert user_data.email is not None
