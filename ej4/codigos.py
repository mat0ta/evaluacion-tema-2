import os
class Codigo():
    def __init__(self, eleccion):
        self.eleccion = int(eleccion)
    def comprobar_excepciones(self):
        if self.eleccion == 1:
            try:
                resultado = 7 / 0
            except ZeroDivisionError:
                print('No se puede dividir entre 0.')
        elif self.eleccion == 2:
            try:
                lista = [4, 7, 30, 23, 5]
                print(lista[10])
            except IndexError:
                print('El índice no existe. Solo hay 5 elementos en la lista.')
        elif self.eleccion == 3:
            try:
                paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
                paises["alemania"]
            except KeyError:
                print('No existe el país. Comprueba que este se encuentra en la lista.')
        elif self.eleccion == 4:
            try:
                resultado = "2" + 10
            except TypeError:
                print('No se puede sumar un string a un numero.')
    def iniciar(self):
        eleccion = 0
        while eleccion != 5:
            eleccion = int(input('Elige una opción:\n1. Division entre 0.\n2. Indice de lista inexistente.\n3. Clave de diccionario inexistente.\n4. Suma de string y numero.\n5. Salir del programa.\nEleccion:'))
            os.system('cls')
            codigo = Codigo(eleccion)
            codigo.comprobar_excepciones()
            print('\n')