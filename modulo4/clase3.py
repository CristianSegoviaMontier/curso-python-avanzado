import random

random_integer = random.randint(1, 20)
print(random_integer)


list_number = []
for i in range(20):
    random_integer = random.randint(1, 20)
    list_number.append(random_integer)

print(list_number)

# Valor random float
random_float = random.random()
print(random_float)

# Lista de rango 10 con valores random float
list_floats = [random.random() for r in range(10)]
print(list_floats)

# Elegir una alternativa
list_text = [random.choice(['a', 'b', 'c', 'd']) for r in range(4)]
print(list_text)

# Generar numeros aleatorios "seguros"
import secrets
random_secure = secrets.token_bytes(4)
print(random_secure)

# Generar ids aleatorios
import uuid
random_uuid = uuid.uuid4()
print(random_uuid)
