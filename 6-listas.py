#   Capítulos 6: Listas
#   Apartado 1: Repaso de conceptos básicos
input("Presiona 'enter' para avanzar al apartado -> 1. Repaso de Conceptos básicos: ")
lista = [1, 2, 3, 4, 5] #   Declaración de una lista
elemento = lista[0]     #   Acceder al elemento de la primera posición de la lista
longitud = len(lista)   #   Número de elementos o longitud de la lista

print("Lista de números: ")
print(lista)
print(f"Primer elemento: {elemento}")
print(f"Longitud de la lista: {longitud}")
print("Iterar sobre los elementos de una lista: ")
for num in lista:       #   Iterar sobre los elementos de una lista
    print(num)



#   Apartado 2: Indexado y sublistas
input("Presiona 'enter' para avanzar al apartado -> 2. Indexado y sublistas: ")
lista = ["Dale", "un", "buen", "like", "al", "vídeo"]
#   En Python, las listas pueden tener índices negativos. Empiezan a contar des del final. 
#   El último elemento está en la posición -1 y el penúltimo en la -2. 

ultimoElemento = lista[-1]  #   Accediendo al último valor de la lista
penultimo = lista[-2]       #   Accediendo al penúltimo valor de la lista

#   Para acceder a un subconjunto de elementos de una lista, utilizamos la nomenclatura:
#   lista[indice_inicio:indice_final]. Esto devuelve una lista con los elementos cuyos 
#   índices se encuentren entre los utilizamos en los brackets.

sublista = lista[2:4]   #   sublista = ["buen", "like"]
sublista2 = lista[:3]   #   Sublista con los elementos de las posiciones 0, 1 y 2. Posición 3 no incluída.
sublista3 = lista[2:]   #   Sublista que empieza en la posición 2, hasta el final de la lista.

sublista4 = lista[-4: -1]   #   Sublista usando índices negativos

print("Lista original: ")
print(lista)
print("Sublista del elemento dos hasta el 3 : ")
print(sublista)
print("Sublista des del inicio hasta el elemento 2: ")
print(sublista2)
print("Sublista des del elemento 2 hasta el final: ")
print(sublista3)
print("Sublista usando índices negativos: ")
print(sublista4)


#   Apartado 3: Comprobar si una lista contiene o no un elemento
input("Presiona 'enter' para avanzar al apartado -> 3. Comprobar si un elemento pertenece o no a la lista: ")
if "like" in lista:
    print("El elemento 'like' pertenece a la lista")

if "manzana" not in lista:
    print("El elemento 'manzana' no está en la lista")


#   Apartado 4: Modificar elementos en una lista
input("Presiona 'enter' para avnazr al apartado -> 4. Modificar elementos de una lista: ")

lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby"]

print("Lista inicial: ")
print(lenguajes)

lenguajes[0] = "C++"    #   Modificar el valor del primer elemento de la lista

print("Lista con el primer elemento modificado: ")
print(lenguajes)

lenguajes[2:4] = ["Anaconda", "TypeScript"]     #   Modificar varios elementos a la vez

print("Lista tras modificar varios elementos a la vez: ")
print(lenguajes)

lenguajes[4:5] = ["C#", "Visual Basic"]
print("Lista tras añadir más de un elemento en una posición")
print(lenguajes)


#   Apartado 5: Métodos de las listas: Añadir elementos
#   En Python podemos utilizar métodos con las listas.
#   Para ejecutar estos métodos: variableDeTipoLista.metodo()
input("Presiona 'enter' para avnazr al apartado -> 5. Métodos de las listas: Añadir Elementos")

lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby"]

print("Lista original: ")
print(lenguajes)


print("Insertar un elemento en una posición determinada, sin borrar ningún otro elemento: ")
lenguajes.insert(1, "C++")  #   Insertamos el elemento "C++" en la posición 1. El resto de elementos se desplazan hacia la derecha
print(lenguajes)

print("Añadir un elemento al final de la lista: ")
lenguajes.append("Scala")   #   Esta función añade un elemento al final de la lista
print("Lenguajes")

print("Añadir una lista a otra: ")
sublista = ["TypeScript", "Matlab", "R"]
print("Lista 1: ")
print(lenguajes)
print("Lista 2: ")
print(sublista)
lenguajes.extend(sublista)
print("Lista combinada: ")
print(lenguajes)


#   Apartado 6: Métodos de las listas: Eliminar elementos elementos
input("Presiona 'enter' para avnazr al apartado -> 6. Métodos de las listas: Eliminar Elementos")
frutas = ["plátano", "kiwi", "papaya", "melocotón", "cereza"]

print("Lista original: ")
print(frutas)

print("Eliminar el último elemento de la lista: ")
elem = frutas.pop()     #   La función pop si argumento elimina y devuelve el último elemento. 
                        
print(f"El elemento {elem} ha sido eliminado de la lista de frutas")
print(frutas)

print("Eliminar el elemento número X de la lista: ")
elem = frutas.pop(2)    #   Se le puede pasar el índice del elemento a eliminar como argumento.
print(f"El elemento {elem} ha sido eliminado de la lista de frutas")
print(frutas)

print("Eliminar un elemento de la lista por su valor: ")
frutas.remove("plátano")    #   La función remove eliminar un elemento por su valor. También lo devuelve
print("Lista con el elemento eliminado: ")
print(frutas)

print("Eliminar el elemento número X de la lista utiizando 'del' : ")
del frutas[0]   #   Eliminar el elemento de la posición 0 mediante la keyword 'del'
print(frutas)

print("Vaciar una lista: ")
frutas.clear()      #   Vaciar todos los elementos de una lista.
print("frutas")


#   Apartado 7: Ejercicio
input("Presiona 'enter' para avnazr al apartado -> 7. Ejercicio")


#   ENUNCIADO: Tenemos un texto dónde queremos encontrar palabras clave. 
#   Las palabras clave pueden ser hasta 5 y deberemos pedírselas al usuario 
#   y guardarlas en una lista. 

#   Si el usuario quiere poner menos de 5 palabras clave, deberá escribir 
#   "fin" para terminar de introducir datos. Si el usuario introduce 
#   números o nada, deberemos eliminarlos de la lista antes de la búsqueda.

#   En otra lista, deberemos guardar el número de veces que aparece cada 
#   palabra clave en nuestro texto. Por ejemplo, si las palabras clave son
#   ordenador y portátil y aparecen 5 y 7 veces respectivamente, nuestras listas
#   deberían ser así: 
#       -   keywords = ["ordenador", "portátil"]
#       -   ocurrencias = [5, 7]


#   Pista: Podemos pasar de una cadena de texto a una lista de palabras mediante
#   el método texto.split(). Por ejemplo:

texto = "hola que tal"
print(texto.split())     

#   SOLUCIÓN: 

texto = """"Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa. 
Es muy importante que logremos teletrabajar efectivamente y de manera autorregulada. 
Esto se traduce en finalizar antes nuestras tareas y evitar jornadas laborales interminables.
El primer consejo y uno de los más importantes ya te lo he dado en el apartado anterior. 
Tenemos que construir un espacio de trabajo en el que nos sintamos cómodos y dispongamos de todas las herramientas necesarias para teletrabajar. 
En la medida de lo posible, es importante teletrabajar siempre en el mismo lugar. 
De esta forma, nuestro cerebro asocia el sitio con la acción de trabajar y nos hará estar más focalizados en nuestras tareas.""" 

keywords = []
ocurrencias = []

#   Obtener palabras clave
keywords = []
ocurrencias = []

for x in range(5):
    keyword = input("Introduce una palabra clave. Si no quieres escribe 'fin': ")
    if keyword == "fin":
        break
    else:
        keywords.append(keyword)

print("Palabras clave introducidas: ")
print(keywords)

posicion = 0

while(True):
    if posicion >= len(keywords):
        break
    if keywords[posicion] == '': 
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric():
        keywords.pop(posicion)
    else:
        posicion += 1


print("Palabras clave corregidas: ")
print(keywords)


texto = texto.replace('.', '').replace(',', '').split()


for x in range(len(keywords)):
    ocurrencias.append(0)

print("Lista de ocurrencias inicializada: ")
print(ocurrencias)

for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            posicion = keywords.index(keyword)
            ocurrencias[posicion] += 1
            break

print("Resultado final: ")
print(keywords)
print(ocurrencias)
