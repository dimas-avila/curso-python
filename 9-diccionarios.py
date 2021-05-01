import os
import logging


#   Capítulos 9: DICCIONARIOS
#   Apartado 1: conceptos básicos

input("Presiona 'enter' para avanzar al apartado -> 1. Conceptos básicos: ")
os.system("cls")

#   Declaración de diccionarios:
#   Los diccionarios son conjuntos de elementos con la estructura clave: valor.
#   Cada elemento de un diccionario contiene una clave y un valor asociado a esta.
#   Las claves pueden ser Strings o int. Los valores pueden ser cualquier tipo de dato.


print("Diccionarios: ")
alejandro = {"Nombre": "Alejandro", "Edad": 30, "Ciudad": "Barcelona",
             "Aficiones": ["videojuegos", "lectura", "cine"]}
print(alejandro)
ana = {"Nombre": "Ana", "Edad": 32, "Ciudad": "Madrid",
       "Aficiones": ["golf", "python", "pesca"]}
print(ana)

#   Los diccionarios pueden contener otros diccionarios:
print("\nDiccionario de diccionarios: ")
trabajadores = {0: alejandro, 1: ana}
print(trabajadores)

#   Los diccionarios no pueden contener claves repetias:
print("\nDiccionario con claves repetidas: ")
a = {
    "año": 1998,
    "año": 2003
}
print(a)

#   Longitud de un diccionario:
print(f"El diccionario tiene {len(alejandro)} elementos")


#   Apartado 2: Añadir, eliminar y modificar elementos de un diccionario


input("Presiona 'enter' para avanzar al apartado -> 2. Añadir, eliminar y modificar elementos de un diccionario: ")
os.system("cls")
print("\nDiccionario original: ")
alejandro = {"Nombre": "Alejandro", "Edad": 30, "Ciudad": "Barcelona",
             "Aficiones": ["videojuegos", "lectura", "cine"]}
print(alejandro)


print("\nAñadir elemento: ")
alejandro["cargo"] = "CEO"
print(alejandro)
print("Añadir un elemento mediante el método 'update': ")
alejandro.update({"sueldo": 2000})
print(alejandro)


print("\nElminar un elemento ")
del alejandro["cargo"]
print(alejandro)
print("Eliminar un elemento mediante el método 'pop': ")
value = alejandro.pop("sueldo")
print(alejandro)
print(value)


print("\nAcceder a un elemento: ")
edad = alejandro["Edad"]
print(f"Tiene {edad} años")
print("Acceder un elemento mediante el método 'get': ")
alejandro.update({"sueldo": 2000})
print(alejandro)


#   Apartado 3: Listas de claves y valores
#   Podemos obtener una lista tanto de las claves como de los valores
#   que conforman un diccionario.

input("Presiona 'enter' para avanzar al apartado -> 3. Listas de claves y valores: ")
os.system("cls")

print("\nLista de claves: ")
claves = alejandro.keys()
print(claves)

print("\nLista de valores: ")
valores = alejandro.values()
print(valores)

#   Podemos iterar en el mismo bucle sobre ambas:

for clave, valor in zip(claves, valores):
    print(f"{clave} --> {valor}")


for clave, valor in alejandro.items():
    print(f"{clave} === {valor}")


#   EJERCICIOS: Buscador de productos. Tenemos varios productos, el usuario
#   mediante el nombre de un producto puede consultar su precio y sus unidades
#   en stock.

pantalones = {
    "nombre": "pantalón",
    "precio": 39.99,
    "stock": 10
}

chaquetas = {
    "nombre": "chaqueta",
    "precio": 59.99,
    "stock": 1
}

bufandas = {
    "nombre": "bufanda",
    "precio": 10.99,
    "stock": 3
}

productos = [
    pantalones,
    chaquetas,
    bufandas
]


def askForInfo(nombreProducto):
    for producto in productos:
        if(producto["nombre"] == nombreProducto):
            return producto["precio"], producto["stock"]
            break
    else:
        return 0, 0


nombre = input("¿Qué producto desea consultar? -> ")
precio, cantidad = askForInfo(nombre)
if precio == 0 and cantidad == 0:
    print("Lo sentimos, el producto que buscas no existe")
else:
    print(
        f"El producto {nombre} vale {precio}€ y disponemos de {cantidad} unidades")
