"""Урок 8.5: Использование фикстуры function_user

Фикстура function_user:
- Создает пользователя перед каждым тестом
- Возвращает UserFixture с request и response
- Убирает дублирование кода создания пользователя
"""
from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentication_client: AuthenticationClient):
    """Тест аутентификации с использованием фикстуры function_user"""
    # Запрос на логин
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    # Выполняем логин
    response = authentication_client.login_api(request)
    # Валидация ответа
    response_data = LoginResponseSchema.model_validate_json(response.text)

    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)

    validate_json_schema(
        instance=response.json(),
        schema=LoginResponseSchema.model_json_schema()
    )
