from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.first_name())
print(fake.last_name())
print(fake.email())
