import unittest
from http import HTTPStatus

import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_get_user_response


class TestUsers(unittest.TestCase):
    def test_create_user(self):
        # Инициализируем API-клиент для работы с пользователями
        public_users_client = get_public_users_client()

        # Формируем тело запроса на создание пользователя
        request = CreateUserRequestSchema()
        # Отправляем запрос на создание пользователя
        response = public_users_client.create_user_api(request)
        # Инициализируем модель ответа на основе полученного JSON в ответе
        # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # Проверяем статус-код ответа
        self.assertEqual(response.status_code, HTTPStatus.OK, 'Некорректный статус-код ответа')

        # Проверяем, что данные ответа совпадают с данными запроса
        self.assertEqual(response_data.user.email, request.email, 'Некорректный email пользователя')
        self.assertEqual(response_data.user.last_name, request.last_name, 'Некорректный last_name пользователя')
        self.assertEqual(response_data.user.first_name, request.first_name, 'Некорректный first_name пользователя')
        self.assertEqual(response_data.user.middle_name, request.middle_name, 'Некорректный middle_name пользователя')


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
