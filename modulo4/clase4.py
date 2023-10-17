import datetime

fecha_hora_actual = datetime.datetime.now()
print('Fecha y hora actual :', fecha_hora_actual)

# Formatear una fecha y hora
formato = "%d/%m/%Y %H:%M:%S"

fecha_formato = fecha_hora_actual.strftime(formato)
print('Fecha formateada :', fecha_formato)

# Fecha especifica
fecha_especifica = datetime.datetime(2022, 8, 12, 15, 30, 0)
print('Fecha y hora especifica :', fecha_especifica.strftime(formato))

# Calculos con fechas
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=23) # para contar cantidad de dias .timedelta(days#)

diff_dates = tomorrow - today
print('Hoy es :', today)
print('Mañana es :', tomorrow)
print('Faltan :', diff_dates.days)


# Convertir string a fecha
fecha_string = '2023-07-12 18:30:00'
fecha_objeto = datetime.datetime.strptime(fecha_string, '%Y-%m-%d %H:%M:%S')

print('Fecha y hora convertida :', fecha_objeto)
print('Tipo de fecha_string :', type(fecha_string))
print('Tipo de fecha_objeto :', type(fecha_objeto))


# Zonas horarias:
import pytz

zona_horaria = pytz.timezone("America/New_York")
fecha_hora_actual = datetime.datetime.now(zona_horaria)
print('Fecha y hora actual en New York :', fecha_hora_actual)


