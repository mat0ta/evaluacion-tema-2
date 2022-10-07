from turtle import color


class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color: {}, Ruedas: {}".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + ", Velocidad: {}, Cilindrada: {}".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        if self.tipo.lower() != "urbana" or self.tipo.lower() != "deportiva":
            print("Tipo de " + type(object).__name__ + " no válido")
    def __str__(self):
        return super().__str__() + ", Tipo: {}".format(self.tipo)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return super().__str__() + ", Carga: {}".format(self.carga)
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + ", Velocidad: {}, Cilindrada: {}".format(self.velocidad, self.cilindrada)


if __name__ == "__main__":
    coche = Coche("Rojo", 4, 160, 1600)
    print(coche)
    bicicleta = Bicicleta("Verde", 2, "Urbana")
    print(bicicleta)
    camioneta = Camioneta("Azul", 4, 180, 2000, 1000)
    print(camioneta)
    motocicleta = Motocicleta("Negra", 2, "Deportiva", 200, 1000)
    print(motocicleta)