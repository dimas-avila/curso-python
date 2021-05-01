import os
import logging


#   Capítulos 16: EXCEPCIONES
#   Las excepciones son errores que ocurren durante la ejecución del
#   programa. Estos errores surgen a pesar de que la sintaxis sea correcta.
#   Ejemplos:
#       - Acceder a una posición de una lista superior a la longitud de esta.
#       - Intentar abrir un fichero que no existe.
#       - Convertir "skdjfajf" a int.
#   IMPORTANTE: Gestionar las excepciones nos permite que el código se siga
#   ejecutando a pesar de que ocurran erroes.


#   Apartado 1: Bloque try: except:
#   Dentro del bloque try, ejecutaremos el código que queremos evaluar (ver
#   si lanza algún error). Dentro del bloque catch

# a = 10/0 (descomentar para ver la excepción que lanza)

def division(a, b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("No se puede dividir por cero")

division(5, 5)
division(5, 0)


#   Apartado 2: Gestión de distintos tipos de excepciones
frutas = ["0-Plátano", "1-Manzana", "2-Pera", "3-Melocotón"]

def elegirFruta(listaFrutas):
    try:
        print(listaFrutas)
        index = int(input("¿Cual es tu fruta favorita? "))
        print(f"Tu fruta favorita es: {listaFrutas[index]}")
    except IndexError:
        print("Esa posición no existe!")
    except ValueError:
        print(f"Tienes que poner un número entre 0 y {len(listaFrutas)-1}")

elegirFruta(frutas)


#   Apartado 3: Excepción Exception. 
#   Las excepciones son objetos que heredan de la clase Exception.
frutas = ["0-Plátano", "1-Manzana", "2-Pera", "3-Melocotón"]

def elegirFruta(listaFrutas):
    try:
        print(listaFrutas)
        index = int(input("¿Cual es tu fruta favorita? "))
        print(f"Tu fruta favorita es: {listaFrutas[index]}")
    except Exception as nombreDelError:
        print(nombreDelError)
        logging.exception("Ha ocurrido el error: ")

elegirFruta(frutas)


#   Apartado 4: Else, Finally, Raise
#   Vamos a sumar los números que nos pase el usuario separados por espacios:

while True:
    try:
        total = 0
        sumandos = input("Introduce valores a sumar separados por un espacio: ")
        sumandos = sumandos.split()
        for num in sumandos:
            if num.isnumeric():
                total += float(num)
            else:
                raise ValueError("El valor no es numérico")
    except ValueError:
        print("Los datos son incorrectos")
        print("Vuelve a introducirlos por favor")
        continue
    else:
        print(f"La suma total es {total}")
        break
    finally:
        print("Ha terminado la iteración...")
        



