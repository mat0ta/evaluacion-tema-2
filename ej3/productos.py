class Producto():
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print('Producto creado con éxito.')
    def __str__(self):
        return 'Nombre: {}\nCodigo: {}\nPrecio {} €\nTipo: {}'.format(self.nombre, self.codigo, self.precio, self.tipo)