from geometria import areas
from geometria.perimetro import perimetro_cuadrado  # funcion especifica de un modulo
from geometria.perimetro import (perimetro_circulo,
                                 perimetro_rectangulo)

area = areas.area_cuadrado(4)
perimetro = perimetro_cuadrado(4)
circulo = perimetro_circulo(10)
rectangulo = perimetro_rectangulo(20, 10)


print('Area del cuadrado :', area)
print('Perimetro del cuadrado :', perimetro)
print('Perimetro del circulo:', circulo)
print('Perimetro del rectangulo :', rectangulo)
