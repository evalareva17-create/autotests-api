from typing import TypedDict, Optional
from httpx import Response
from clients.api_client import APIClient

class CreateExerciseRequest(TypedDict):
    title: str
    courseId: str
    description: str
    maxScore: Optional[int]
    minScore: Optional[int]
    orderIndex: Optional[int]
    estimatedTime: Optional[str]

class UpdateExerciseRequest(TypedDict, total=False):
    title: str
    description: str
    maxScore: int
    minScore: int
    orderIndex: int
    estimatedTime: str

class ExercisesClient(APIClient):
    def get_exercises_api(self, course_id: str, token: str) -> Response:
        """
        Получение списка заданий для определенного курса.
        GET /api/v1/exercises

        :param course_id: ID курса, для которого нужно получить задания.
        :param token: Токен авторизации.
        :return: Объект Response с данными ответа.
        """
        headers = {"Authorization": f"Bearer {token}"}
        params = {"courseId": course_id}
        return self.get("/api/v1/exercises", params=params, headers=headers)

    def get_exercise_api(self, exercise_id: str, token: str) -> Response:
        """
        Получение информации о задании по exercise_id.
        GET /api/v1/exercises/{exercise_id}

        :param exercise_id: ID задания.
        :param token: Токен авторизации.
        :return: Объект Response с данными ответа.
        """
        headers = {"Authorization": f"Bearer {token}"}
        return self.get(f"/api/v1/exercises/{exercise_id}", headers=headers)

    def create_exercise_api(self, request: CreateExerciseRequest, token: str) -> Response:
        """
        Создание задания.
        POST /api/v1/exercises

        :param request: Данные для создания задания (TypedDict).
        :param token: Токен авторизации.
        :return: Объект Response с данными ответа.
        """
        headers = {"Authorization": f"Bearer {token}"}
        return self.post("/api/v1/exercises", json=request, headers=headers)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequest, token: str) -> Response:
        """
        Обновление данных задания.
        PATCH /api/v1/exercises/{exercise_id}

        :param exercise_id: ID задания.
        :param request: Данные для обновления задания (TypedDict).
        :param token: Токен авторизации.
        :return: Объект Response с данными ответа.
        """
        headers = {"Authorization": f"Bearer {token}"}
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request, headers=headers)

    def delete_exercise_api(self, exercise_id: str, token: str) -> Response:
        """
        Удаление задания.
        DELETE /api/v1/exercises/{exercise_id}

        :param exercise_id: ID задания.
        :param token: Токен авторизации.
        :return: Объект Response с данными ответа.
        """
        headers = {"Authorization": f"Bearer {token}"}
        return self.delete(f"/api/v1/exercises/{exercise_id}", headers=headers)
