import unittest
from http import HTTPStatus

import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_get_user_response
from tools.fakers import fake


@pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
def test_create_user(domain: str, public_users_client: PublicUsersClient):
    """Тест создания пользователя с параметризацией домена email"""
    # Формируем тело запроса с email с указанным доменом
    request = CreateUserRequestSchema(email=fake.email(domain=domain))
    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)
    # Валидация ответа
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)

    # Проверяем, что данные ответа совпадают с данными запроса
    assert response_data.user.email == request.email
    assert response_data.user.last_name == request.last_name
    assert response_data.user.first_name == request.first_name
    assert response_data.user.middle_name == request.middle_name


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user: UserFixture, private_users_client: PrivateUsersClient):
    """Тест получения текущего пользователя через /api/v1/users/me"""
    # Выполняем запрос
    response = private_users_client.get_user_me_api()
    # Валидация ответа
    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(response_data, function_user.response)

    validate_json_schema(
        instance=response.json(),
        schema=GetUserResponseSchema.model_json_schema()
    )
