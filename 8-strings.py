import os
import logging
#   Capítulos 7: Métodos de Strings
#   Apartado 1: Métodos find, index y count

#   Los métodos find e index sirven para encontrar conjuntos
#   de caracteres dentro de un string (por ejemplo, una 
#   palabra dentro de una frase)

input("Presiona 'enter' para avanzar al apartado -> 1. Métodos find, index y count: ")
os.system("cls")

#   Vamos a usar los métodos para comprobar que una dirección de correo
#   contiene una '@' y únicmaente una.

mail = "correo@gmail.com"

#   En caso de encontrar el substring, ambos métodos hacen los mismo. 
posFind = mail.find("@")
posIndex = mail.index("@")
print(f"La posición encontrada con find es: {posFind}.\nLa posición encontrada con index es: {posIndex}")

#   En caso de no encontrar el substring, find devuelve -1 pero index lanza un error. 
posFind = mail.find("*")
print(f"La posición encontrada es: {posFind}")
try:
    posIndex = mail.index("*")
except BaseException:
    logging.exception("Ha ocurrido el siguiente error: ")

#   Para comprobar que únicamente aparece una vez, usamos el método count:
apariciones = mail.count('@')
print(f"El caracter '@' aparece {apariciones} veces")


#   Apartado 2: Métodos split, replace y join:

#   El método split sirve para dividir un string mediante un delimitador
#   y convertir cada división en un elemento de una lista. 

#   El método replace sirve para reemplazar un substring por otro.

#   El método join sirve para unir una lista de strings en un único string
#   mediante un caracter determinado. 

input("Presiona 'enter' para avanzar al apartado -> 2. Métodos split, replace y join: ")
os.system("cls")

compra = "chocolate, pan, agua, plátanos, verduras, pipas, orégano"
print(compra)

#   ¿Cómo podemos saber cuántas cosas hay que comprar? 
listaCompra = compra.split(', ')
numeroElementos = len(listaCompra)
print(listaCompra)
print(numeroElementos)

#   Uso del método replace para separar los elementos mediante '-' en vez de ','.
print("Modificamos el separador de los elementos del string 'compra': ")
compra = compra.replace(', ', ' - ')
print(compra)

#   Uso del método join para convertir una lista en un string
compra = "/".join(listaCompra)
print(compra)



#   EJERCICIO: Tenemos unas descripciones de algunos productos. 
#   En ellas se incluye el precio de cada producto. Debemos encontrar
#   el precio en € y mostrarlo por pantalla. El precio puede tener: 
#   0,1 o 2 decimales y siempre va seguido del símbolo '€'. Por ejemplo: 
#
#       -   9.99€
#       -   10€
#       -   10.5€

#   BONUS: Deberemos modificar las descripciones para que el precio
#   se muestre en dólares. La conversión es: 1€ = 1.21$. No hace falta
#   modificar la variable original de la descripición, podemos retornar
#   una copia con el precio convertido.


#   SOLUCIÓN:

des1 = "Este bolso de cuero de la marca: Miguel Cors tiene un precio de 199.99€. Es una oferta especial."
des2 = "Las botas de la marca: Nique valen 89€. Nunca han estado tan rebajadas."
des3 = "¡Tenemos el bambú en oferta! Cómpralo ahora por 1.2€ el kg ¡No la dejes pasar!"

def findPriceAndReplace(txt):
    txtList = txt.split()
    pos = -1
    indx = -1
    conversion = 1.21
    for palabra in txtList:
        pos = palabra.find("€")
        if pos != -1:
            indx = txtList.index(palabra)
            break
    precio = txtList[indx]
    precio = precio.split('€')[0]
    txtList[indx] = str(float(precio)*conversion) + '$'
    newDesc = " ".join(txtList)
    return precio, newDesc

precio, newDesc = findPriceAndReplace(des1)
print(precio)
print(newDesc)
precio, newDesc = findPriceAndReplace(des2)
print(precio)
print(newDesc)
precio, newDesc = findPriceAndReplace(des3)
print(precio)
print(newDesc)



#   Apartado 3: Otros métodos útiles
#   En este apartado veremos algunos métodos que pueden ser de 
#   utiliadad para manipular strings. 

input("Presiona 'enter' para avanzar al apartado -> 3. Otros métodos útiles ")
os.system("cls")

texto = "esto Es un texto de Ejemplo"
print("\nMétodo startswith: comprobar si un string empieza con el valor especificado")
print(texto.startswith('e'))
print("\nMétodo upper: Retorna una copia del string en mayúsculas")
print(texto.upper())
print("\nMétodo title: Retorna una copia del string pero la primera letra de cada palabra está en mayúsculas")
print(texto.title())
print("\nMétodo capitalize: Retorna una copia del string con la primera letra en mayúsculas")
print(texto.capitalize())
print("\nMétodo rjust: Retorna una copia del string con X caracteres justificado hacia la derecha")
print(texto.rjust(len(texto) + 8))


#   EJERCICIO: Formatear texto. Debemos formatear el siguiente texto siguiente 
#   una serie de normas: 
#       -   '#' a principio de línea significa que es un título y deberemos convertirlo 
#           todo a mayúsculas.
#       -   '##' a principio de línea significa que es un subtítulo y deberemos poner la
#            primera letra de cada palabra en mayúsculas.
#       -   '###' deberemos poner únicamente la primera letra en mayúsculas.
#       -   si la línea empieza con '-' deberemos añadir una sangría.

#   NOTA: El método splitlines() retorna una lista de strings. Separa mediante saltos de línea.
#   SOLUCIÓN:

texto = """
#este es el título principal

- Esto es una lista.
- De cosas que podemos hacer.

##este es un subtítulo

Esto es una pequeña introducción.
- Esto es otra lista
- De más cosas que podemos hacer.
"""

def formatText(txt):
    txtList = txt.splitlines()
    for indx in range(len(txtList)):
        if(txtList[indx].startswith('###')):
            txtList[indx] = txtList[indx].replace('###', '')
            txtList[indx] = txtList[indx].capitalize()
        elif(txtList[indx].startswith('##')):
            txtList[indx] = txtList[indx].replace('##', '')
            txtList[indx] = txtList[indx].title()
        elif(txtList[indx].startswith('#')):
            txtList[indx] = txtList[indx].replace('#', '')
            txtList[indx] = txtList[indx].upper()
        elif(txtList[indx].startswith('-')):
            txtList[indx] = txtList[indx].rjust(len(txtList[indx]) + 8)
    return '\n'.join(txtList)

print(formatText(texto))