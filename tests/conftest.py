"""
Урок 8.5: Хранение фикстур в conftest.py

conftest.py - специальный файл для хранения фикстур:
- Фикстуры доступны автоматически без импорта
- Можно создавать на разных уровнях (глобальные и локальные)
- Централизует общие фикстуры для повторного использования

Особенности:
- Глобальная доступность: фикстуры доступны в том же каталоге и подкаталогах
- Нет импорта: pytest автоматически обнаруживает фикстуры
- Упрощение структуры: общие фикстуры в одном месте
"""

import pytest
from pydantic import BaseModel, EmailStr

from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.fakers import fake


# ============================================================================
# МОДЕЛИ ДЛЯ ФИКСТУР
# ============================================================================

class UserFixture(BaseModel):
    """Модель для агрегации данных пользователя из фикстуры"""
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        """Быстрый доступ к email пользователя"""
        return self.request.email

    @property
    def password(self) -> str:
        """Быстрый доступ к password пользователя"""
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        """Данные для аутентификации пользователя"""
        return AuthenticationUserSchema(email=self.email, password=self.password)


# ============================================================================
# ГЛОБАЛЬНЫЕ ФИКСТУРЫ (доступны во всех тестах проекта)
# ============================================================================


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    """Фикстура для получения клиента аутентификации"""
    return get_authentication_client()


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    """Фикстура для получения публичного клиента пользователей"""
    return get_public_users_client()


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура для создания пользователя (scope='function')
    
    Название: {scope}_{сущность}
    - function - пользователь создается перед каждым тестом
    - user - создаваемая сущность
    
    Возвращает UserFixture с request и response для удобного доступа к данным
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Фикстура для получения приватного клиента пользователей с аутентификацией
    Использует authentication_user из function_user для аутентификации
    """
    return get_private_users_client(function_user.authentication_user)


# Пример 5: Автоматическая фикстура (autouse=True)
@pytest.fixture(autouse=True)
def test_logging():
    """
    Фикстура выполняется автоматически перед каждым тестом
    Не требует явной передачи в тест
    """
    print("\n--- Начало теста ---")
    yield
    print("\n--- Конец теста ---")


# Пример 6: Фикстура уровня класса (scope="class")
@pytest.fixture(scope="class")
def class_setup():
    """Выполняется один раз для каждого тестового класса"""
    print("\nSetup для класса")
    yield
    print("\nTeardown для класса")
