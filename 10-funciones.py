import os
import logging
#   Capítulos 10: Funciones - Capítulo dos: argumentos arbitrarios y keyword arguments
#
#   Apartado 1: Argumentos arbitrarios:
#   Los argumentos arbitrarios se utilizan cuando no sabemos
#   de forma exacta el número de parámetros que la función va a
#   recibir.


input("Presiona 'enter' para avanzar al apartado -> 1. Argumentos arbitrarios ")
os.system("cls")

def maximo(*args):
    maximo = args[0]
    for arg in args[1:]:
        if arg > maximo:
            maximo = arg
    return maximo

print("El máximo es: ")
print(maximo(0, 90, 23, 11, 10, -5))
print("El máximo es: ")
print(maximo(0, 110, 23, 110.45, 10.23, -10, 33, 55))


def formatoDescarga(tipo, *args):
    numArgs = len(args)
    if tipo == "video":
        if numArgs == 0:
            print(f"El formato seleccionado es:\n-Tipo de archivo: {tipo}")
        if numArgs == 1:
            resolucion = args[0]
            print(f"El formato seleccionado es:\n-Tipo de archivo: {tipo}\n-Resolución: {resolucion}")
        elif numArgs == 2: 
            resolucion = args[0]
            fps = args[1]
            print(f"El formato seleccionado es:\n-Tipo de archivo: {tipo}\n-Resolución: {resolucion}\n-FPS: {fps}")
    elif tipo == "audio":
        print(f"El formato seleccionado es:\n-Tipo de archivo: {tipo}")
    else:
        print("Error: el formato que pides no existe.")

formatoDescarga("audio")
formatoDescarga("video", 720)
formatoDescarga("video", 1080, 60)


#   Apartado 2: Keyword Arguments:

#   Podemos pasar los argumentos de una función
#   mediante keywords. De esta forma conseguimos
#   que el orden de los argumentos sea indiferente.

input("Presiona 'enter' para avanzar al apartado -> 2. Keyword Arguments ")
os.system("cls")


def crearPersonaje(clase, raza, nombre):
    print(f"{nombre} es un {clase} de raza {raza}")

crearPersonaje(clase="mago", nombre="Thorofin", raza="Elfo")
crearPersonaje(nombre="Askland", clase="Pícaro",  raza="Humana")


#   Apartado 3: Keyword Arbitrary Arguments:

#   Se utilizan cuando no sabemos cuántos argumentos 
#   de palabra clave vamos a recibir

def printKwargs(**kwargs):
    print("\n")
    print("Los atributos del personaje son:")
    for clave, valor in kwargs.items():
        print(f"{clave} ---> {valor}")
    

printKwargs(clase="mago", nombre="Thorofin", raza="Elfo")
printKwargs(clase="mago", nombre="Thorofin", raza="Elfo", mascota="Dragón", nivel="165", clan="ValenciaFC")


#   Apartado 4: Combinación de todos los anteriores
#   Se pueden usar conjuntamente en una misma función


def crearPersonaje(nombre, *args, **kwargs):
    descripcion = "##### " + nombre.upper() + " #####\n\n"
    descripcion += "##### DESCRIPCIÓN #####\n\n"
    for clave, valor in kwargs.items():
        descripcion += f"- {clave} ---> {valor}\n"
    
    descripcion += "\n##### HABILIDADES #####\n\n"

    for skill in args:
        descripcion += f"- {skill}\n"
    return descripcion


pj = crearPersonaje("Dandelion", "ataque fuerte", "esquivar", "bomba de humo", raza="Elfo", mascota="Dragón", nivel="165", clan="ValenciaFC")
print(pj)