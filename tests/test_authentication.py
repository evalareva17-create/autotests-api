from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    # 1. Инициализация клиентов
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    # 2. Создание пользователя
    create_user_request = CreateUserRequestSchema(
        email=fake.email(),
        password=fake.password(),
        last_name=fake.last_name(),
        first_name=fake.first_name(),
        middle_name=fake.middle_name()
    )
    public_users_client.create_user(create_user_request)

    # 3. Аутентификация
    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    login_response = authentication_client.login_api(login_request)

    # 4. Проверка статус-кода
    assert_status_code(login_response.status_code, HTTPStatus.OK)

    # 5. Десериализация ответа
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    # 6. Проверка тела ответа
    assert_login_response(login_response_data)

    # 7. Валидация JSON-схемы
    validate_json_schema(
        instance=login_response.json(),
        schema=LoginResponseSchema.model_json_schema()
    )
