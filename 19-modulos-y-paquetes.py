#   Capítulos 19: Módulos y Paquetes
#   Apartado 1: Módulos y Paquetes
#   Los módulos son archivos de Python (o de Cpython o de C). 
#   Estos archivos pueden contener funciones, clases y variables.
#   Podemos importarlas a nuestros archivos para hacer uso de estas
#   sin tener que volver a escribir su código. 

import paquete.moduloAreas
from paquete.moduloAreas import areaTriangulo
from paquete.moduloPerimetros import CalculadorDePerimetros as CP


print(paquete.moduloAreas.PI)
print(paquete.moduloAreas.areaCirculo(3))
print(areaTriangulo(3, 4))

#   Los paquetes son conjuntos de módulos, relacionados entre sí,
#   en un mismo directorio.

cp = CP()
print(cp.perimetroCuadrado(5))


#   Apartado 2: Indexado y sublistas

#   En Python, las listas pueden tener índices negativos. Empiezan a contar des del final. 
#   El último elemento está en la posición -1 y el penúltimo en la -2. 