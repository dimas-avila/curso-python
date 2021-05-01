import os
#   Capítulos 6: Strings
#   Apartado 1: Repaso de conceptos básicos

#   Distintas formas de declarar Strings

input("Presiona 'enter' para avanzar al apartado -> 1. Repaso de Conceptos básicos: ")
os.system("cls")
texto = "¿Hola qué tal?"
print("Texto simple: ")
print(texto)

#   Si queremos mostrar comillas dobles en nuestro texto: ""
#   deberemos envolver el texto en comillas simples ->
comillasSimples = 'el personaje afirmó "me convertiré en rey" rotundamente'
print("Texto que contiene comillas dobles: ")
print(comillasSimples)

#   Si queremos mostrar comillas simples en nuestro texto: ""
#   deberemos envolver el texto en comillas dobles ->
comillasDobles = "el personaje afirmó 'me convertiré en rey' rotundamente"
print("Texto que contiene comillas simples: ")
print(comillasDobles)

#   Para crear un texto formateado (saltos de línea, sangrías)
#   deberemos envolver el texto en TRES comillas dobles ->

textoFormateado = """
====== TEXTO FORMATEADO =======
Podemos poner:
    - Saltos de línea.
    - Tabulaciones.
=============================== 
"""
print("Texto formateado: ")
print(textoFormateado)


#   Conversión de datos numéricos a Strings
numeroEntero = 7
numeroDecimal = 3.14

print("Tipo de dato antes de la conversión: ")
print(type(numeroEntero))
print(type(numeroDecimal))

strNumeroEntero = str(numeroEntero)     
strNumeroDecimal = str(numeroDecimal)

print("Tipo de dato después de la conversión: ")
print(type(strNumeroEntero))
print(type(strNumeroDecimal))

#   Conversión de booleanos a Strings
print("También podemos convertir booleanos por ejemplo: ")
print(type(str(True)))

#   Número de caracteres en un string: 
texto = "123456789"
longitudTexto = len(texto)
print("La variable 'texto' contiene: " + str(longitudTexto) + " caracteres")

#   Concatenar Strings:
texto1 = "012345"
texto2 = "6789"
textoConcatenado = "Números del 0 al 9" + texto1 + texto2 
print(textoConcatenado)



#   Apartado 2: Los strings son listas
#   En este apartado descubriremos que realmente los strings son Arrays
#   o vectores (similar a las listas). 

input("Presiona 'enter' para avanzar al apartado -> 2. Los Strings son listas: ")
os.system("cls")
texto = "0123456789"
print("Texto original:\n" + texto)

#   Acceder al primer carácter de un String
primerCaracter = texto[0]
print("Primter caracter: ")
print(primerCaracter)

#   Acceder a un subgrupo de catacteres de un String
subString = texto[1:6]
print("Substring: ")
print(subString)

#   Iterar sobre un String:
print("Iterar sobre un string: ")
texto = "0123456789"
for num in texto:
    print("Valor actual: " + num)

#   EJERCICIO (mini): Tenemos un string únicamente compuesto por números enteros. 
#   Debemos sumar su valor uno a uno y mostrar por pantalla la suma
#   total de todos los números.

valores = "984823185"
print("Ejercicio:  Sumar todos los números del string -> " + valores)

#   Solución:

total = 0
for valor in valores: 
    total += int(valor)

print(f"El total es: {total}")



#   Apartado 3: Format Strings
#   Nos permiten generar strings combinando texto con 
#   otras variables de forma sencilla y legible. 

input("Presiona 'enter' para avanzar al apartado -> 3. Format Strings: ")
os.system("cls")

cantidad = 5
precio = 15.80

print("Forma cutre: ")
print("Has comprado " + str(cantidad) + " unidades. Cada unidad vale " + str(precio) + "€. En total son: "+ str(cantidad*precio) +"€")

print("Forma avanzada: ")
formatString = "Has comprado {} unidades. Cada una vale {}€. En total son {}€".format(cantidad, precio, cantidad*precio)
print(formatString)

print("God mode: ")
print(f"Has comprado {cantidad} unidades. Cada una vale {precio}€. En total son {precio*cantidad}€")