from turtle import color


class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        if self.ruedas and self.color:
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
        if tipo.lower() != "urbana" or tipo.lower() != "deportiva":
            super().__init__(color, ruedas)
            self.tipo = tipo
        else:
            print("Tipo de bicicleta no válido")
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
        if tipo.lower() == "urbana" or tipo.lower() == "deportiva":
            super().__init__(color, ruedas, tipo)
            self.velocidad = velocidad
            self.cilindrada = cilindrada
        else:
            print("Tipo de motocicleta no válido")
    def __str__(self):
        if self.cilindrada and self.velocidad:
            return super().__str__() + ", Velocidad: {}, Cilindrada: {}".format(self.velocidad, self.cilindrada)


if __name__ == "__main__":
    coche = Coche("Rojo", 4, 210, 2500)
    print(coche)
    bicicleta = Bicicleta("Rojo", 2, "Urbanoide")
    print(bicicleta)
    camioneta = Camioneta("Rojo", 4, 210, 2500, 3000)
    print(camioneta)
    motocicleta = Motocicleta("Rojo", 2, "Deportivoide", 200, 1000)
    print(motocicleta)