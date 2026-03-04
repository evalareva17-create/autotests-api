import unittest
from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


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
