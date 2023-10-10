# concatenacion
cadena1 = 'Hola,'
cadena2 = '¿Como estas?'
resultado = cadena1 + cadena2
print(resultado)
print(resultado.upper())  # metodo de python para string


#nombre = input("Ingresa tu nombre :")
#apellido = input("Ingresa tu apellido :")
#edad = int(input("Edad :"))
#print ('Hola mi nombre es ' + nombre + " " + apellido)

# F strings
#saludo = f'Hola minombre es {nombre} {apellido} y tengo {edad} años'
#print(saludo)

# Concatenar con listas
numeros = [1,2,3,4,5]
resultado =''

for num in numeros:
    resultado += str(num) + " "
print(resultado)


# Concatenacion con Join
palabras = ['Hola ' 'Mundo','Python']
frase=' '.join(palabras)
print(frase)