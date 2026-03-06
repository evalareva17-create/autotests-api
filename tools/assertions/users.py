from clients.users.users_schema import UserSchema, CreateUserResponseSchema, GetUserResponseSchema, CreateUserRequestSchema
from tools.assertions.base import assert_equal


def assert_user(actual: UserSchema, expected: UserSchema) -> None:
    """Проверяет корректность данных пользователя"""
    assert_equal(actual.id, expected.id, "Некорректный id пользователя")
    assert_equal(actual.email, expected.email, "Некорректный email пользователя")
    assert_equal(actual.last_name, expected.last_name, "Некорректный last_name пользователя")
    assert_equal(actual.first_name, expected.first_name, "Некорректный first_name пользователя")
    assert_equal(actual.middle_name, expected.middle_name, "Некорректный middle_name пользователя")


def assert_get_user_response(
    get_user_response: GetUserResponseSchema,
    create_user_response: CreateUserResponseSchema
) -> None:
    """Проверяет, что данные пользователя при создании и при запросе совпадают"""
    assert_user(get_user_response.user, create_user_response.user)


def assert_create_user_response(
    request: CreateUserRequestSchema,
    response: CreateUserResponseSchema
) -> None:
    """Проверяет, что данные пользователя при создании совпадают с запросом"""
    assert_equal(response.user.email, request.email, "Некорректный email пользователя")
    assert_equal(response.user.last_name, request.last_name, "Некорректный last_name пользователя")
    assert_equal(response.user.first_name, request.first_name, "Некорректный first_name пользователя")
    assert_equal(response.user.middle_name, request.middle_name, "Некорректный middle_name пользователя")
