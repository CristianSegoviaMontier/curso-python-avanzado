import math

# constantes matematicas:
print('pi : ', math.pi)
print('numero de Euler', math.e)

# Funciones trigonometricas

angulo = math.radians(45)
print(angulo)
print('Seno :', math.sin(angulo))
print('Coseno :', math.cos(angulo))
print('Tangente :', math.tan(angulo))

# Funciones Exponenciales
print('Exponencial (e^2): ', math.exp(2))

# Funciones Logaritmicas
print('Log de 10 :', math.log(10))

# Potencias
print('2 elevado al cubo :', math.pow(2, 3))

# Raices
print('Raiz cuadrada de 25 :', math.sqrt(25))

# Fracciones
from fractions import Fraction

frac1 = Fraction(3, 4)
frac2 = Fraction(1, 6)

suma = frac1 + frac2
resta = frac1 - frac2
multi = frac1 * frac2
division = frac1 / frac2
print('Fraccion 1 :', frac1)
print('Fraccion 2: ', frac2)
print('Suma :', suma)
print('Resta :', resta)
print('Multiplicacion :', multi)
print('Division :', division)

# trabajo con decimales especiales - mayor detalle de decimales:
# Libreria
from decimal import Decimal, getcontext

getcontext().prec = 20

num1 = Decimal('0.00000011111111')
num2 = Decimal('0.000000003343333')

print('Numero1 :', num1)
print('Numero2 :', num2)

suma_decimal = num1 + num2
print('Suma Decimal: ', suma_decimal)
