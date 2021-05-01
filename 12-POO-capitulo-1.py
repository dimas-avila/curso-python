class Camiseta:
    """
    Clase camiseta: Representa una camiseta de la vida real.
    =======================================================

    Atributos: 
    ----------

    - precio -> (float) almacena el precio de la camiseta.
    - marca -> (str) almacena el marca de la camiseta.
    - talla -> (str) almacena el talla de la camiseta.
    - color -> (str) almacena el color de la camiseta.
    - rebajada -> (bool) inidica si está o no rebajada.

    Métodos:
    --------

    - __init__(precop, marca, talla, color) -> (Camiseta) constructor de la clase.
    - aplicarDescuento(porcentaje) -> descuenta el *porcentaje* al precio de la camiseta.
    - teñir(color) -> cambia el color de la camiseta
    - infoCamiseta() -> (str) retorna la descripción de la camiseta
    """
    def __init__(self, precio, marca, talla, color):
        self.precio = precio
        self.marca = marca
        self.talla = talla
        self.color = color
        self.rebajada = False


    def aplicarDescuento(self, porcentaje):
        nuevoPrecio = self.precio - self.precio*porcentaje/100
        self.precio = nuevoPrecio
        if porcentaje < 100:
            self.rebajada = True


    def teñir(self, color):
        self.color = color


    def infoCamiseta(self):
        info = f"Camiseta:\nTalla: {self.talla}\nPrecio: {self.precio:.2f}€\nMarca: {self.marca}\n"
        if self.rebajada:
            info += "Actualmente esta camiseta está rebajada"
        return info



camiseta = Camiseta(19.99, "Gucci", "XL", "Negro")
print(camiseta.infoCamiseta())
camiseta.aplicarDescuento(20)
print(camiseta.infoCamiseta())

print("\n####################\n")
camisetaAdimas = Camiseta(300, "Adimas", "M", "Rojo")
print(camisetaAdimas.color)
print(camisetaAdimas.marca)
camisetaAdimas.teñir("Verde")
print(camisetaAdimas.color)