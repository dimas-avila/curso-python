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
for x in range(5):
    keyword = input("Introduce una palabra clave o 'fin' si ya no quieres poner más: ")
    if keyword == "fin":
        break
    else:
        keywords.append(keyword)

print("Palabras clave introducidas")

#   Eliminar números o strings vacíos
for keyword in keywords:
    if keyword == '' or keyword.isnumeric():
        keywords.remove(keyword)


#   Inicializamos la lista de ocurrencias y preparamos el texto

texto = texto.replace('.', '').replace(',', '').split()
for x in range(len(keywords)):
    ocurrencias.append(0)


for palabra in texto:
    for keyword in keywords: 
        if palabra == keyword:
            ocurrencias[keywords.index(keyword)] += 1
            break

print(keywords)
print(ocurrencias)