texto = """
Python es uno de los lenguajes de programación dinámicos más populares 
que existen entre los que se encuentran Java, Javascript, Go y C#. 
Aunque es considerado a menudo como un lenguaje "scripting", 
es realmente un lenguaje de propósito general. En la actualidad, 
Python es usado para todo, desde simples "scripts", 
hasta grandes servidores web que proveen servicio ininterrumpido 24×7. 
Es utilizado para la programación de interfaces gráficas y bases de datos, 
programación web tanto en el cliente como en el servidor (véase Django o Flask) y 
testing de aplicaciones. Además tiene una amplia aceptación por científicos que 
hacen aplicaciones para las supercomputadores más rápidas del 
mundo y por los niños que recién están comenzando a programar."""

palabra_busqueda = input('Ingrese palabra a buscar :')
index = texto.find(palabra_busqueda) #busca solo la primera ocurrencia

if (index != -1):
    print(f"{palabra_busqueda} se encontro en el indice {index}")

    total_encontrado = texto.count(palabra_busqueda)
    print(f'{palabra_busqueda} aparece {total_encontrado} veces en el texto')
else:
    print(f'Palabra {palabra_busqueda} no encontrada')

texto2=texto.replace('Python', 'python', 1) # solo reemplaza una vez lo encontrado (de izquierda a derecha)

nuevo_texto = texto.upper()
print(nuevo_texto)

print(texto2)