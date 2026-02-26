import httpx

# 1. Данные для входа
payload_login = {
  "email": "user@example.com",
  "password": "string"
}

# 2. Логинимся
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_login)
login_data = login_response.json()

# 3. Достаем токен (структура ответа: {'token': {'accessToken': '...', ...}})
token = login_data['token']['accessToken']

# 4. Делаем запрос /me с токеном
headers = {"Authorization": f"Bearer {token}"}
me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(me_response.json())
