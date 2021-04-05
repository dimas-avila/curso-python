#   Capítulo 3: Booleanos, condicionales y entrada de usuario.

#   Entrada de datos del usuario. Identificación del tipo de datos.
edad = input("Introduce tu edad por favor: ")
tipo_de_dato = type(edad)
print(edad)
print(tipo_de_dato)


#   BOOLEANOS, IF
verdadero = True
falso = False

if(verdadero == True):
    print("Soy verdadero")

if(falso == True):
    print("Eiiii")

if(falso == False):
    print("Efectivamente, falso es falso")


#   Operadores de Compraración ==, !=, <, >, >=, <=
edad = input("Introduce tu edad por favor: ")
edad = int(edad)

if(edad >= 18):
    print("Eres mayor de edad, puedes entrar")
elif(edad < 0):
    print("Eso es imposible")
elif(edad < 15):
    print("Eres muy muy pequeño")
else:
    print("Eres menor, no puedes entrar")

print("Fin del if")


#   Operadores Lógicos and, or, not
edad = input("Introduce tu edad por favor: ")
edad = int(edad)
if(type(edad) == int):
    if(edad > 120 or edad < 0):
        print("No me lo creo")
    elif(edad > 18 and edad < 65):
        print("Eres adulto")
    elif(edad < 18 and edad > 15):
        print("Eres un adolescente")
    else:
        print("Pues nada")
else:
    print("Tu edad debería ser un número entero")


#   Ejercicio: Comprobar si un número introducido por el usuario es par.
#              si el usuario no introduce un número, o el número es decimal
#              el programa debe avisar de que los datos no son correctos.

# PISTAS:
#   isdigit, isdecimal, num%2 = 0

# SOLUCIÓN
num = input("Introduce un número: ")

if(not(num.isnumeric())):
    print("Datos incorrectos. El número debe ser un entero")
else:
    num = int(num)
    if(num%2 == 0):
        print("El número es par")
    else:
        print("El número es impar")
    



