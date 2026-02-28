import httpx
from clients.users.public_users_client import PublicUsersClient
from clients.exercises.exercises_client import ExercisesClient

# 1. Настройка клиентов
base_url = "http://localhost:8000"
http_client = httpx.Client(base_url=base_url)
public_users_client = PublicUsersClient(http_client)
exercises_client = ExercisesClient(http_client)

# 2. Создаем пользователя и логинимся (чтобы получить токен)
user_data = {
    "email": "exercise_tester@example.com",
    "password": "password123",
    "lastName": "Tester",
    "firstName": "Exercise",
    "middleName": "Testovich"
}
# Создаем (игнорируем ошибку, если уже есть)
public_users_client.create_user_api(user_data)

# Логинимся
login_response = http_client.post("/api/v1/authentication/login", json={"email": user_data["email"], "password": user_data["password"]})
token = login_response.json()["token"]["accessToken"]
print(f"Токен получен: {token[:10]}...")

# 3. Создаем курс (нужен для упражнения)
# Используем прямой запрос, так как CoursesClient у нас пока нет
course_data = {
    "title": "Test Course for Exercises",
    "description": "Description",
    "courseType": "PUBLIC",
    "isActive": True
}
headers = {"Authorization": f"Bearer {token}"}
course_response = http_client.post("/api/v1/courses", json=course_data, headers=headers)
course_id = course_response.json()["course"]["id"]
print(f"Курс создан: {course_id}")

# 4. Тестируем ExercisesClient

# 4.1 Создание упражнения
exercise_data = {
    "title": "Test Exercise",
    "courseId": course_id,
    "description": "Do something cool",
    "maxScore": 10,
    "minScore": 0,
    "orderIndex": 1,
    "estimatedTime": "1h"
}
create_resp = exercises_client.create_exercise_api(exercise_data, token)
print("\nСоздание упражнения:", create_resp.status_code)
print(create_resp.json())
exercise_id = create_resp.json()["exercise"]["id"]

# 4.2 Получение списка упражнений
list_resp = exercises_client.get_exercises_api(course_id, token)
print("\nСписок упражнений:", list_resp.status_code)
print(f"Найдено упражнений: {len(list_resp.json()['exercises'])}")

# 4.3 Получение одного упражнения
get_resp = exercises_client.get_exercise_api(exercise_id, token)
print("\nПолучение упражнения:", get_resp.status_code)
print(get_resp.json())

# 4.4 Обновление упражнения
update_data = {"title": "Updated Exercise Title"}
update_resp = exercises_client.update_exercise_api(exercise_id, update_data, token)
print("\nОбновление упражнения:", update_resp.status_code)
print(update_resp.json())

# 4.5 Удаление упражнения
delete_resp = exercises_client.delete_exercise_api(exercise_id, token)
print("\nУдаление упражнения:", delete_resp.status_code)

# Проверяем, что удалилось
check_resp = exercises_client.get_exercise_api(exercise_id, token)
print("Проверка после удаления (должно быть 404):", check_resp.status_code)

http_client.close()
