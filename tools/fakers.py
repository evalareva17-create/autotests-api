import time
from faker import Faker


def get_random_email() -> str:
    return f"tests.{time.time()}@example.com"


class Fake:
    """
    Класс для генерации случайных данных
    """

    def __init__(self, faker: Faker):
        """
        Инициализация класса
        :param faker: экземпляр класса Faker для генерации данных
        """
        self.faker = faker

    def text(self) -> str:
        """
        Метод для генерации случайного текста
        :return: Случайный текст
        """
        return self.faker.text()

    def sentence(self) -> str:
        """
        Метод для генерации случайного предложения
        :return: Случайное предложение
        """
        return self.faker.sentence()

    def uuid4(self) -> str:
        """
        Метод для генерации случайного UUID
        :return: UUID строка
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def password(self) -> str:
        """
        Метод для генерации случайного пароля
        :return: Пароль строка
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Метод для генерации случайной фамилии
        :return: Фамилия
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Метод для генерации случайного имени
        :return: Имя
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Метод для генерации случайного отчества
        :return: Отчество
        """
        try:
            return self.faker.middle_name()
        except AttributeError:
            return self.faker.first_name()

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Метод для генерации случайного числа
        :param start: Начало диапазона
        :param end: Конец диапазона
        :return: Случайное число
        """
        return self.faker.random_int(min=start, max=end)

    def estimated_time(self) -> str:
        """
        Метод для генерации времени выполнения
        :return: Строка времени (например, "5 weeks")
        """
        return f"{self.integer(1, 10)} weeks"

    def max_score(self) -> int:
        """
        Метод для генерации максимального балла
        :return: Число от 50 до 100
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Метод для генерации минимального балла
        :return: Число от 0 до 30
        """
        return self.integer(0, 30)


# Создаем экземпляр с русской локалью
fake = Fake(Faker('ru_RU'))
