import numpy as np

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros)

# Usando numpy
np_numeros = list(np.arange(1,10))
print(np_numeros)

# Matrices

lista_matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(lista_matriz)
print(matriz)
print('Tipo de matriz :', type(matriz))

# Suma de matrices
suma = matriz[0] + matriz[2]
print(suma)

# Suma de valores puntuales de una matriz
suma_valor = matriz[0,0] + matriz[1,2]
print(suma_valor)

# Calculos estadisticos
data = np.array([12,13,20,18,30,22,19,])

# Media
mean = np.mean(data)
print('Media :', mean)

# Desviación estandar
std = np.std(data)
print('Desviación Estandar :',std)

# Maximos y posicion del maximo
max_val = np.max(data)
max_index = np.argmax(data)
