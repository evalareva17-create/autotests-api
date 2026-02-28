from httpx import Client


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client без аутентификации.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        base_url="http://localhost:8000",
        timeout=100
    )
