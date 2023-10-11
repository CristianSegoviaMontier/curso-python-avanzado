import re


cadena = 'vamos a aprender expresiones regulares con python'

busqueda = re.search('aprender', cadena) # el resultado es un objeto, por tanto tiene metodos que se pueden utilizar
print(busqueda)

# busqueda de fechas en base a un patron:
texto ='La fecha de vencimiento es 2023-12-31 y la fecha de inicio fue el 2023-01-15'

patron_fecha = r'\d{4}-\d{2}-\d{2}' # 4 digitos - 2 digitos - 2 digitos

fechas_encontradas = re.findall(patron_fecha,texto)
print(fechas_encontradas)


# Reemplazo de texto basado en patrones:
texto = 'el numero de telefono es 211-374-1234'
patron_numero = r'\d{3}-\d{3}-\d{4}'

nuevo_texto = re.sub(patron_numero,'####',texto)
print(texto)
print(nuevo_texto)

# Extraccion de urls desde un texto:
html = '<p>Enlace uno <a href="http://www.google.com">Enlace1</a>'
patron_url = r'<a href="(.*?)">(.*?)</a>'
enlaces = re.findall(patron_url,html)

for enlace in enlaces:
    url,texto=enlace
    print(f'URL :{url}, texto :{texto}')