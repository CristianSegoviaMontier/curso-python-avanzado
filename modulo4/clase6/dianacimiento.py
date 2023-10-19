'''
Ingresar fecha y que arroje el dia de nacimiento
'''
import datetime


def dia_nacimiento(fecha_nacimiento):
    dias = ['domingo', 'lunes' 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']
    index_dia = fecha_nacimiento.weekday()
    return dias[index_dia]


if __name__ == '__main__':
    fecha_string = input('Ingrese su fecha de nacimiento (YYY-MM-DD):')
    fecha_objeto = datetime.datetime.strptime(fecha_string, '%Y-%m-%d')
    dia = dia_nacimiento(fecha_objeto)
    print(f'Tu fecha de nacimiento es {fecha_string} y tu dia de nacimiento es : {dia}')
