#   Capítulo 16: Funciones MAP y FILTER
#   Son funciones que sirven para trabajar con iteradores.
#   Vienen incorporadas por defecto con python.

#   Apartado 1: Función filter
#   filter(function, iterable). Devuelve un iterador 
#   con los valores del iterable que cumplan la función. 
import math

emails = [
    "hola@gmail.com", 
    "juan@hotmail.es",
    "parateletrabajo.es",
    "mandarinas",
    "casatere@soporte.net"
    ]

def checkMail(mail):
    if '@' in mail:
        return True
    else:
        return False

def checkMail2(mail):
    return '@' in mail

#   Uso de la función filter para
#   comprobar emails válidos de una lista.
validMails = filter(checkMail, emails)
print(list(validMails))


#   Uso de la función filter con una función lambda
validMails = filter(lambda x: ('@' in x), emails)
print(list(validMails))


#   Apartado 2: Función map
#   map(function, iterable). 
#   Ejecuta la función usando como parámetro
#   cada elemento del iterable.

palabras = (
    "dale",
    "un",
    "like",
    "y",
    "suscríbete"
)

resultado = map(lambda x: len(x), palabras)
print(list(resultado))

eje_x = [0,1,2,3,4,5,6,7,8,9,10]
eje_y = map(lambda x, y: round(math.cos(x) + math.exp(y), 3), eje_x, eje_x)
print(list(eje_y))

