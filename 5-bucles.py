#   Capítulo 5: Bucles

#   Breve introducción a las listas
numeros = [0, 1, 2, 3, 4, 5]
nombres = ["Jorge", "Juan", "Javier", "Jairo"]
variada = ["Juan", 3, False, True, 2, "arroz"]

longitudnumeros = len(numeros)
longitudnombres = len(nombres)
longitudvariada = len(variada)

print(longitudnumeros)
print(numeros)
print(longitudnombres)
print(nombres)
print(longitudvariada)
print(variada)

#   Elementos de una lista
print("Primer elemento de numeros")
print(numeros[0])
print("Último elemento de nombres")
print(nombres[longitudnombres-1])


#   Bucles: Bucle for
for x in range(5):
    print(x)

for letra in "Dimas":
    print(letra)

#   Mini ejemplo, imprimir solo las vocales de una palabra

for letra in "cococdrilo":
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(letra)
    else:
        print("No es una vocal")

#   Mini ejemplo, iterar sobre una lista
print("Lista original de numeros: ")
print(numeros)

for num in numeros:
    print(num)
    num += 10

print("Lista modificada de numeros: ")
print(numeros)


#   Bucles While
i = 0
while(i < 10):
    print(i)
    i += 1

letraEncontrada = False
letra = "a"
frase = "En este momento estoy buscando la letra a"
pos = 0

while(not(letraEncontrada)):
    if(frase[pos] == "a"):
        letraEncontrada = True
        print(f"Encontrada la letra {letra} en la posición {pos}")
    else:
        pos += 1

#   Break, continue, pass
frase = "No sé cuando encontraré la letra a"
letra = "a"

#   Break
for x in frase:
    if(x == "a"):
        print(f"Encontrada en la posición: {frase.index(x)}")
        break

#   Continue
frase = "Hola Ana"
count = 0
for x in frase:
    if(x == "a"):
        count = count + 1
        continue
    print("No hemos encontrado nada")
print(count)

#   Pass
frase = "frase corta"
for x in frase:
    if(x == "a"):
        pass
    print("Seguimos con la iteración")

#   Else
frase = "Quiero contar todas las a de esta frase"
count = 0

for x in frase:
    if(x == "a"):
        count = count + 1
        continue
    print("No hemos encontrado nada")
else:
    print(f"Hemos encontrado {count} veces la letra a")


#   Ejercicio: El usuario debe adivinar un número entre 0 y 10.
#   El programa deberá pedir que el usuario introduzca un número
#   y debe decir si ha acertado, si el número es menor o mayor que
#   el que ha introducido.

def pedirYComprobar(numero):
    num = int(input("Introduce el número: "))
    if(num == numero):
        print("Has acertado")
        return True
    elif(numero > num):
        print("Casi! Prueba con un número más grande")
        return False
    elif(numero < num):
        print("Casi! Prueba con un número pequeño")
        return False

while(True):
    if(pedirYComprobar(7)):
        break
else:
    print("Cuando hay un break, no se ejecuta el else")
    

while(not(pedirYComprobar(7))):
    pass