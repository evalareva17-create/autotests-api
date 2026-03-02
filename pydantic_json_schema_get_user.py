from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

# 1. Создаем пользователя
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# 2. Аутентифицируемся
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

# 3. Получаем данные пользователя (используем _api метод для получения Response)
user_id = create_user_response.user.id
get_user_response = private_users_client.get_user_api(user_id)

# 4. Генерируем JSON Schema
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# 5. Валидируем ответ
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)


