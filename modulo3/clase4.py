name = "Cristian"
age = 42
print(f"Mi nombre es {name} y tengo {age} años")

print("Mi nombre es {} y tengo {} años".format(name,age+10))
#muy usado para secuencias SQL

sql_insert = "insert into users (nama,age) values ('{}','{}')".format(name,age)

print(sql_insert)

print("Nombre : {1}, Edad : {1}".format(name,age))

# Print con parametros
producto = 'Celular Iphone 12'
precio = 599.99
print("Producto : {prod}, PRecio : {pre}".format(prod = producto, pre = precio))

# Formatear numeros
num = 12345.6789
print("{:.2f}".format(num))  # dos decimales
print("{:,}".format(num))  # sep de miles
print("{:e}".format(num))  # notacion cientifica

# Formatear fechas
from datetime import datetime
now = datetime.now()
print('Fecha y hora : {:%d/%m/%Y %H:%M:%S}'.format(now))
print('Fecha : {:%Y-%m-%d}'.format(now))

# Alineacion y relleno:
number = 42
print('Numero : {:>10}'.format(number))
print('Numero : {:0>5}'.format(number))

numero_folio = '{:0>4}'.format(number)
print(numero_folio)
print(type(numero_folio))