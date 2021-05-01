#   Capítulo 20: Archivos externos
#   Apartado 1: Abrir y leer un documento existente.


#   Por defecto, el modo de abrir un fichero es lectura
#   como texto. Por tanto para leer su contenido no 
#   es necesario especificar el segundo argumento. 
fichero = open('./demo.txt', 'rt', encoding='utf-8') # r-> read, t-> text-mode

#   Para leer línea a línea podemos usar el método
#   readline. Cada llamada nos devolverá una nueva línea
#   hasta llegar al final del fichero

"""firstLine = fichero.readline()
secondLine = fichero.readline()
print(firstLine)
print(secondLine)"""

#   Para leer todas las líneas (restantes) de un fichero, 
#   podemos utilizar el método readlines. Nos 
#   retorna una lista cuyos elementos son líneas
#   del fichero.

todasLasLineas = fichero.readlines()
print("Fichero línea a línea: ")
print(todasLasLineas)

#   Debemos cerrar el fichero una vez hayamos terminado
fichero.close()


#   Apartado 2: Escribir en un fichero existente
#   Si un fichero ya tiene contenido, tenemos dos opciones:
#   Sobreescribir el contenido, o añadir el contenido 
#   nuevo al final del que ya existe. Modo write: 

fichero = open('./demo.txt', 'wt', encoding='utf-8')  # w->write, t-> text-mode

numeroBytes = fichero.write("Acabo de cargarme todo el contenido del fichero.\n")
print(f"Hemos escrito {numeroBytes}B")

nuevoConenido = [
    "Podemos escribir el contenido mediante una lista.\n",
    "No olvidéis añadir los saltos de línea.\n",
    "No se añaden automáticamente.\n"
]

fichero.writelines(nuevoConenido)

fichero.write("Voy a escribir una línea más por si acaso.\n")

fichero.close()

#   Apartado 3: Escribir en un fichero existente.
#   Modo APPEND. Nos sirve para añadir contenido
#   sin eliminar el existente:

fichero = open('./demo.txt', 'at', encoding='utf-8')
fichero.write("\n\nPuedo añadir una línea nueva sin borrar las anteriores.\n")
fichero.close()


#   Apartado 4: Crear un nuevo fichero.
#   Cuando usamos open en modo create, 
#   podemos escribir en el fichero tras crearlo
#   pero no leer.

#   Si intentamos crear un fichero que ya existe,
#   saltará una excepción.

try:
    fichero = open('./demo3.txt', 'xt', encoding='utf-8')
    fichero.write("Hola qué tal")
    fichero.close()
except FileExistsError:
    print("No hemos podido crear el fichero porque ya existe.")


#   Apartado 5: Método seek. Podemos controlar 
#   la posición desde la cual empezamos a leer.

fichero = open('./demo.txt', 'rt', encoding='utf-8')
fichero.seek(20)

print("\nFichero empezando en el caracter número 20: \n")

print(fichero.read())
fichero.close()


#   Apartado 6: Lectura y escritura simultáneas.

fichero = open('./demo.txt', 'r+', encoding='utf-8')

lineas = fichero.readlines()
print(lineas)

fichero.write("\nUna nueva línea.\n")
fichero.close()


#   Apartado 7: Ejercicio Resuelto.
#   ENUNCIADO: Queremos comparar el tiempo que 
#   tarda en sumar todos los elementos de una
#   una lista un bucle for y un bucle
#   while. 

#   Para ello, debemos calcular el tiempo empleado 
#   en cada bucle varias veces y luego promediarlo.
#   Debemos cronometrar lo que tarda cada bucle 100 veces
#   y guardar cada resultado en un fichero.


import time
import random
#   lista que deberemos sumar
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(50000):
    lista.append(random.randint(0, 10000))
fichero = open('times.txt', 'wt', encoding='utf-8')


#   Paso 1: Recopilar y escribir los datos
for x in range(100):
    #   suma total para el bucle for
    accFor = 0
    startTime = time.time()
    for num in lista:
        accFor = accFor + num
    elapsedTimeFor = time.time() - startTime 

    pos = 0
    #   suma total para el bucle while
    accWhile = 0
    startTime = time.time()
    while pos < len(lista):
        accWhile = accWhile + lista[pos]
        pos = pos + 1
    elapsedTimeWhile = time.time() - startTime
    fichero.write(f"{elapsedTimeFor};{elapsedTimeWhile}\n")
fichero.close()


#   Paso 2: Leer datos y calcular el tiempo medio

fichero = open('times.txt', 'rt', encoding='utf-8')

meanFor = 0
meanWhile = 0
samples = 0

for line in fichero.readlines():
    line.replace('\n','')
    timeFor, timeWhile = line.split(';')
    meanFor += float(timeFor)
    meanWhile += float(timeWhile)
    samples += 1

print(f"Tiempo medio bucle for: {(meanFor/samples)*(10**3)}ms. Tiempo medio bucle while: {(meanWhile/samples)*(10**3)}ms")

fichero.close()





