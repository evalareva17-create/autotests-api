import httpx
from tools.fakers import get_random_email

# 1. Создаем пользователя
create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "tester",
  "firstName": "auto",
  "middleName": "test"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print('create_user_response_data:', create_user_response_data)

# 2. Логинимся
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print('login_response_data:', login_response_data)

# 3. Получаем данные пользователя (GET)
get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

user_id = create_user_response_data['user']['id']
get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{user_id}", headers=get_user_headers)
get_user_response_data = get_user_response.json()

print('get_user_response_data:', get_user_response_data)

# 4. Удаляем пользователя (DELETE)
delete_user_response = httpx.delete(f"http://localhost:8000/api/v1/users/{user_id}", headers=get_user_headers)

print('delete_user_response status:', delete_user_response.status_code)
