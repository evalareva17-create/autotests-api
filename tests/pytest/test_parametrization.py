"""
Урок: Параметризация в pytest

Параметризация позволяет запускать один тест с разными данными:
- Экономия времени: один тест покрывает несколько вариантов
- Поддерживаемость: меньше дублирования кода
- Гибкость: легко добавлять новые данные
"""
import pytest
from _pytest.fixtures import SubRequest


# ============================================================================
# 1. Базовый случай - один параметр
# ============================================================================

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    """Тест выполнится 4 раза с разными значениями number"""
    assert number > 0


# ============================================================================
# 2. Несколько параметров
# ============================================================================

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    """Возводим число в квадрат и проверяем результат"""
    assert number ** 2 == expected


# ============================================================================
# 3. Перемножение параметров (декартово произведение)
# ============================================================================

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(os: str, host: str):
    """Тест выполнится 12 раз (4 os × 3 hosts)"""
    assert len(os + host) > 0


# ============================================================================
# 4. Параметризация фикстур
# ============================================================================

@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest) -> str:
    """Фикстура вернет три разных хоста"""
    return request.param


def test_host(host: str):
    """Автотест автоматически параметризован из фикстуры"""
    print(f"Running test on host: {host}")


# ============================================================================
# 5. Параметризация классов
# ============================================================================

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    """Параметр user передается в каждый метод класса"""

    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")
