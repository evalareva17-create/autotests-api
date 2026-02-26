import httpx
from tools.fakers import get_random_email

# 1. Создаем пользователя
create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "New",
  "firstName": "User",
  "middleName": "Userovich"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Создан пользователь:", create_user_response_data)

user_id = create_user_response_data['user']['id']

# 2. Логинимся, чтобы получить токен
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
token = login_response_data['token']['accessToken']
headers = {"Authorization": f"Bearer {token}"}

# 3. Обновляем данные пользователя (PATCH)
update_user_payload = {
  "lastName": "Updated",
  "firstName": "User",
  "middleName": "Userovich"
}
update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", json=update_user_payload, headers=headers)
update_user_response_data = update_user_response.json()

print("Обновленный пользователь:", update_user_response_data)
