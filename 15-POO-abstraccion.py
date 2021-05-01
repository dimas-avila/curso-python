from abc import ABC, abstractmethod


class Personaje(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []

    @abstractmethod
    def atacar(self, objetivo):
        pass
        
    @abstractmethod
    def getStatus(self):
        print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")

    
    def subirDeNivel(self):
        self.nivel += 1
        print(f"El nivel actual de {self.nombre} es {self.nivel}")


    def verInventario(self):
        print(f"Inventario de {self.nombre}: ")
        for objeto in self.inventario:
            print(objeto)



class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 100
        self.inteligencia = 120
        self.inventario = ["Poción de maná", "Grimorio"]

    def getStatus(self):
        print("Clase: Mago")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.inteligencia*0.6
        print(f"Vida actual del objetivo: {objetivo.vida}")



class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Poción de vida", "Maza", "Escudo"]

    def getStatus(self):
        print("Clase: Guerrero")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza*0.85
        print(f"Vida actual del objetivo: {objetivo.vida}")

    
    

guerrero = Guerrero("Kaladin")
mago = Mago("Yuno")


guerrero.getStatus()
mago.getStatus()

guerrero.verInventario()
mago.verInventario()

mago.atacar(guerrero)
guerrero.atacar(mago)