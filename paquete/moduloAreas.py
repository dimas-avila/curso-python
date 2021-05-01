#   Módulo para calcular áreas de figuras geométricas
PI = 3.1415 # Constante

def areaCirculo(radio):
    return PI * radio**2


def areaTriangulo(base, altura):
    return base * altura/2


def areaCuadrado(lado):
    return lado * lado
