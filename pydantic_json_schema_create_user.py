from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password=fake.password(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name()
)
create_user_response = public_users_client.create_user_api(create_user_request)

# Получаем JSON-схему из Pydantic-модели ответа
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

# Проверяем, что JSON-ответ от API соответствует ожидаемой JSON-схеме
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)

print("Validation successful!")
