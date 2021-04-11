#   Capítulo 4: Funciones
#   Definición de las funciones
def saludar():
    print("Hola ¿Qué tal?")

print("Apartado 1: Funciones básicas. Función para saludar")
saludar()
saludar()


#   Funciones con argumentos
def saludar(nombre):
    print("Hola "+nombre+" ¿Qúe tal?")

print("Apartado 2: Funciones con argumentos. Saludar con nombre")
saludar("Marta")
saludar("Juan")


#   Funciones con retorno
def suma(a, b):
    resultado = a + b
    return resultado

def sumaDos(a, b):
    return a+b

print("Apartado 3: Funciones que retornan un valor. Función para sumar dos números")
print(suma(2, 2))
print(sumaDos(2, 2))


#   Funciones con argumentos con valor por defecto
def saludarPorDefecto(nombre="Dimas"):
    print("Hola "+nombre+" ¿Qúe tal?")

print("Apartado 4: Funciones con argumentos por defecto. Función para saludar")
saludarPorDefecto()
saludarPorDefecto("Ana")


#   Funciones que retornan varios valores
def sumaYResta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

print("Apartado 5: Funciones con múltiples retornos. Función para saludar")
resultadoSuma, resultadoResta = sumaYResta(10, 5)
print("El resultado de la suma es: " + str(resultadoSuma) + "\n Y el de la resta: " + str(resultadoResta))

#   EJERCICIO 1: Función máximo -> Dados dos números, la función debe encontrar cuál de los dos
#   es el más grande y retornarlo.Extra: Se deben comprobar que los argumentos de la función sean
#   de tipo int o float. Si alguno de los dos no lo es, mostrar un mensaje de error y retornar False.
#   #SOLUCIÓN

def maximo(num1, num2):
    if((type(num1)==int or type(num1)==float) and (type(num2)==int or type(num2)==float)):
        if(num1 > num2):
            return num1
        else:
            return num2
    else:
        print("Los argumentos no son válidos")
        return False

print("Apartado 6: Ejercicio 1. Encontrar el máximo de dos números")

num = maximo(5, 1)
if(type(num) != bool):
    print("El máximo es: " + str(num))

num = maximo("hola", 2)
if(type(num) != bool):
    print("El máximo es: " + str(num))



#   EJERCICIO 2: Mini calculadora. Pedirle al usuario una operación y dos números. 
#   Las operaciones pueden ser suma, resta, potencia. Si introduce una operación diferente
#   a estas, mostrar un mensaje de error. Si la operación es correcta, mostrar el resultado.


#   #SOLUCIÓN
def calculadora():
    operacion = input("¿Qué operación quieres hacer?Las operaciones posibles son:\n-suma\n-resta\n-potencia\n")
    num1 = float(input("Introduce el primer valor: "))
    num2 = float(input("Introduce el segundo valor: "))
    if(operacion == "suma"):
        print(num1 + num2) 
    elif(operacion == "resta"):
        print(num1 - num2) 
    elif(operacion == "potencia"):
        print(num1**num2) 
    else:
        print("Operación errónea. Las operaciones posibles son:\n-suma\n-resta\n-potencia\n")

print("Apartado 6: Ejercicio 2. Mini calculadora")
calculadora()