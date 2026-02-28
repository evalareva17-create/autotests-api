from typing import TypedDict, Optional, List
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка заданий.
    """
    exercises: List[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения задания.
    """
    exercise: Exercise


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    description: str
    maxScore: int
    minScore: int
    orderIndex: int
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания задания.
    """
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict, total=False):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str
    description: str
    maxScore: int
    minScore: int
    orderIndex: int
    estimatedTime: str


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании.

        :param exercise_id: ID задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с данными задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления данных задания.

        :param exercise_id: ID задания.
        :param request: Словарь с обновленными данными.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: ID задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # Добавляем новые методы с типизацией

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения списка заданий с типизированным ответом.

        :param query: Словарь с courseId.
        :return: Словарь с данными списка заданий.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения задания с типизированным ответом.

        :param exercise_id: ID задания.
        :return: Словарь с данными задания.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод создания задания с типизированным ответом.

        :param request: Словарь с данными задания.
        :return: Словарь с данными созданного задания.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод обновления задания с типизированным ответом.

        :param exercise_id: ID задания.
        :param request: Словарь с обновленными данными.
        :return: Словарь с данными обновленного задания.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Данные пользователя для аутентификации.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
