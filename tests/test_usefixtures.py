"""
Урок 8.5: Использование pytest.mark.usefixtures

pytest.mark.usefixtures позволяет:
- Подключать фикстуры без указания их в параметрах теста
- Применять фикстуры к целым классам
- Упрощать код, когда фикстуры не возвращают значения
"""
import pytest


# Фикстура для очистки данных из базы данных
@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")


# Фикстура для заполнения данных в базу данных
@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")


# Пример 1: Подключение одной фикстуры к тесту
@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    """Тест использует фикстуру fill_books_database без явного указания в параметрах"""
    pass


# Пример 2: Подключение нескольких фикстур к классу
@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    """Все тесты в классе используют обе фикстуры"""

    def test_read_book_from_library(self):
        pass

    def test_delete_book_from_library(self):
        pass
