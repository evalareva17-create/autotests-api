"""
Урок: Параметризация в pytest

Параметризация позволяет запускать один тест с разными данными:
- Экономия времени: один тест покрывает несколько вариантов
- Поддерживаемость: меньше дублирования кода
- Гибкость: легко добавлять новые данные
"""
import pytest


# ============================================================================
# 1. Параметризация тестов с @pytest.mark.parametrize
# ============================================================================

@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("admin", "admin123")
])
def test_login_parametrized(username, password):
    """Тест выполнится 3 раза с разными username и password"""
    assert username is not None
    assert password is not None


# ============================================================================
# 2. Параметризация с pytest.param и маркерами
# ============================================================================

@pytest.mark.parametrize("value", [
    pytest.param(1, id="positive"),
    pytest.param(2, id="positive_two"),
    pytest.param(-1, marks=pytest.mark.skip(reason="Negative value"), id="negative"),
])
def test_increment(value):
    """Третий тест будет пропущен"""
    assert value > 0


# ============================================================================
# 3. Параметризация со словарями
# ============================================================================

@pytest.mark.parametrize("data", [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "admin", "password": "admin123"},
])
def test_login_with_dict(data):
    """Параметризация с использованием словарей"""
    assert data["username"] is not None
    assert data["password"] is not None


# ============================================================================
# 4. Комбинированная параметризация
# ============================================================================

@pytest.mark.parametrize("host", ["localhost", "example.com"])
@pytest.mark.parametrize("port", [1000, 2000, 3000])
def test_client_combinations(host, port):
    """Тест выполнится 6 раз (2 hosts × 3 ports)"""
    assert host in ["localhost", "example.com"]
    assert port in [1000, 2000, 3000]


# ============================================================================
# 5. Параметризация фикстур
# ============================================================================

@pytest.fixture(params=[1000, 2000, 3000])
def port_fixture(request):
    """Фикстура с параметризацией"""
    return request.param


def test_port_from_fixture(port_fixture):
    """Тест выполнится 3 раза с разными портами из фикстуры"""
    assert port_fixture in [1000, 2000, 3000]


# ============================================================================
# 6. Параметризация с несколькими параметрами
# ============================================================================

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (10, -5, 5),
    pytest.param(0, 0, 0, id="zeros"),
])
def test_addition(a, b, expected):
    """Тест сложения с разными значениями"""
    assert a + b == expected
