import os
import logging
#   Capítulos 11: Tuplas
#
#   Apartado 1: Tuplas - Conceptos básicos. 
#   Las tuplas son conjuntos ordenados de datos que no se pueden modificar.


input("Presiona 'enter' para avanzar al apartado -> 1. Tuplas - Conceptos básicos ")
os.system("cls")

mitupla = ("BadBunny", "Anuel", "Daddy Yankee", "Wisin")
print("El valor de mitupla es: ")
print(mitupla)
print(f"La longitud de mitupla es: {len(mitupla)}")

print("Iterar sobre una tupla: ")
for cantante in mitupla:
    print(f"Cantante número {mitupla.index(cantante)}: {cantante}")


#   Apartado 2: Indexado de Tuplas

#   Podemos indexar los elementos de una tupla de la misma
#   forma que las litas. 
input("Presiona 'enter' para avanzar al apartado -> 2. Indexado de Tuplas ")
os.system("cls")

mitupla = ("BadBunny", "Anuel", "Daddy Yankee", "Wisin")
print("El valor de mitupla es: ")
print(mitupla)

primero = mitupla[0]
print(f"Primer elemento de la tupla: {primero}")

ultimo = mitupla[-1]
print(f"Último elemento de la tupla: {ultimo}")

print("Subtupla")
subtupla = mitupla[1:3]
print(subtupla)


#   Apartado 3: Modificar tuplas

#   No podemos modificar directamente una tupla. Veremos 
#   qué errores ocurren y cómo transformar una tupla a 
#   una lista y viceversa. 
input("Presiona 'enter' para avanzar al apartado -> 3. Modificar Tuplas ")
os.system("cls")

mitupla = ("BadBunny", "Anuel", "Daddy Yankee", "Wisin")
print("El valor de mitupla es: ")
print(mitupla)

try:
    del mitupla[2]
except BaseException:
    logging.exception("El error cuando intentamos eliminar un elemento de una tupla es: ")

try:
    mitupla.append("Yandel")
except BaseException:
    logging.exception("El error cuando intentamos añadir un elemento nuevo a una tupla es: ")

try:
    mitupla[3] = "Yandel"
except BaseException:
    logging.exception("El error cuando intentamos modificar un elemento nuevo a una tupla es: ")


print("\n\nConvertir tupla -> lista: ")
milista = list(mitupla)
print(milista)
print("Añadimos un nuevo elemento a la lista: ")
milista.append("Yandel")
print(milista)
print("Convertimos la lista a una tupla: ")
mitupla = tuple(milista)
print(mitupla)
print("Unir varias tuplas: ")
mitupla2 = ("Don Omar", "Tego Calderon", "Kendo Kapone")
mitupla3 = mitupla + mitupla2
print(mitupla3)


#   Apartado 4: Empaquetar y desempaquetar tuplas

#   De la misma forma que podemos agrupar múltiples 
#   variables en una tupla (empaquetar), también podemos
#   asignar cada elemento de una tupla a una variable distinta.
   

input("Presiona 'enter' para avanzar al apartado -> 4. Empaquetar y desempaquetar tuplas")
os.system("cls")

mitupla = ("BadBunny", "Anuel", "Daddy Yankee")
print("El valor de mitupla es: ")
print(mitupla)
print("Desempaquetar los elementos contenidos en una tupla")
(artista1, artista2, artista3) = mitupla
print("Artista 1: {}. Artista 2 {}. Artista 3: {}".format(artista1, artista2, artista3))

mitupla = ("BadBunny", "Anuel", "Daddy Yankee", "Myke Towers", "Farruko", "C.Tangana")
print("El valor de mitupla es: ")
print(mitupla)
print("Desempaquetar: ")

(primerArtista, segundoArtista, *variosArtistas) = mitupla
print(f"Primer artista: {primerArtista}. Segundo Artista {segundoArtista}. Varios artistas: ")
print(variosArtistas)


(primerArtista, *variosArtistas, ultimoArtista) = mitupla
print(f"Primer artista: {primerArtista}. Último Artista {ultimoArtista}. Varios artistas: ")
print(variosArtistas)


#   Apartado 5: *Extra* Listas de tuplas

#   Podemos crear listas cuyos elementos 
#   sean tuplas. De esta forma, podemos 
#   iterar sobre las diversas tuplas
#   y además desempaquetar sus elementos. 

comida = [("primero", "macarrones"), ("segundo", "pollo"), ("postre", "flan")]
print("El menú de hoy es: ")

for plato, nombre in comida:
    print(f"{plato} --> {nombre}")


#   De hecho, esto es lo que realmente ocurre
#   cuando utilizamos el método items sobre un diccionario.
    
artistas = {1: "C.Tangana", 2: "Duki", 3: "Khea"}
print("Artistas: ")
print(artistas)

listaTuplas = artistas.items()
print(listaTuplas)


for clave, valor in listaTuplas:
    print(f"{clave}: {valor}")


