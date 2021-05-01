class Empleado:

    def __init__(self, nombre, sueldoMensual):
        self.nombre = nombre
        self.sueldoMensual = sueldoMensual

    
    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1 + 1/100)
        print(f"El sueldo anual de {self.nombre}, empleado estándar, es {sueldo}€")



class Contable(Empleado):

    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)
        
    
    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1 + 4/100)
        print(f"El sueldo anual de {self.nombre}, Contable, es {sueldo}€")



class Publicista(Empleado):

    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    
    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1 + 4/100)
        print(f"El sueldo anual de {self.nombre},  Publicista, es {sueldo}€")

    
class Becario(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    
    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual
        print(f"El sueldo anual de {self.nombre},  Becario, es {sueldo}€")



empleado = Empleado("Juan", 1000)
publicista = Publicista("Mario", 1200)
contable = Contable("Ángela", 1300)
becario = Becario("Ryan", 750)

empleados = [empleado, publicista, contable, becario]
for x in empleados:
    x.calcularSueldoAnual()