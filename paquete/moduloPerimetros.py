#   Módulo para calcular perímetros 
import math
class CalculadorDePerimetros:
    def __init__(self):...

    def perimetroCuadrado(self, lado):
        return 4*lado

    def perimetroTriangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3

    def perimetroCirculo(self, radio):
        return 2*math.pi*radio