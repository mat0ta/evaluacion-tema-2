from turtle import color

vehiculos_creados = []
class Vehiculo():
    global vehiculos_creados
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        if self.ruedas and self.color:
            return "Color: {}, Ruedas: {}".format(self.color, self.ruedas)
    def catalogar(self, ruedas_elegidas = None):
        cuenta = 0
        for i in vehiculos_creados:
            if i[1] == ruedas_elegidas:
                cuenta += 1
        print("Se han encontrado {} vehículos con {} ruedas:".format(cuenta, ruedas_elegidas))

class Coche(Vehiculo):
    global vehiculos_creados
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        vehiculos_creados.append([color, ruedas, velocidad, cilindrada])
    def __str__(self):
        return super().__str__() + ", Velocidad: {} km/h, Cilindrada: {} cc".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):
    global vehiculos_creados
    def __init__(self, color, ruedas, tipo):
        if tipo.lower() == "urbana" or tipo.lower() == "deportiva":
            super().__init__(color, ruedas)
            self.tipo = tipo
            vehiculos_creados.append([color, ruedas, tipo])
        else:
            self.nottipo = tipo
    def __str__(self):
        try:
            return super().__str__() + ", Tipo: {}".format(self.tipo)
        except AttributeError:
            return "Tipo de bicicleta no válido (" + self.nottipo + ")"

class Camioneta(Coche):
    global vehiculos_creados
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
        vehiculos_creados.append([color, ruedas, velocidad, cilindrada, carga])
    def __str__(self):
        return super().__str__() + ", Carga: {} kg".format(self.carga)
    
class Motocicleta(Bicicleta):
    global vehiculos_creados
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        if tipo.lower() == "urbana" or tipo.lower() == "deportiva":
            super().__init__(color, ruedas, tipo)
            self.velocidad = velocidad
            self.cilindrada = cilindrada
            vehiculos_creados.append([color, ruedas, tipo, velocidad, cilindrada])
        else:
            self.nottipo = tipo
    def __str__(self):
        try:
            return super().__str__() + ", Velocidad: {} km/h, Cilindrada: {} cc".format(self.velocidad, self.cilindrada)
        except AttributeError:
            return "Tipo de motocicleta no válido (" + self.nottipo + ")"