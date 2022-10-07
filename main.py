import os
import sys
import pathlib

from ej5.vehiculos import Vehiculo
for i in range(5):
    sys.path.append(str(pathlib.Path().resolve()) + '/ej' + str(i + 1))
    print('Path del ejercicio ' + str(i + 1) + ' añadido.')
print('Todos los paths han sido añadidos.\n')
from alumnos import Alumno
from alumnos_str import Alumno_str
from productos import Producto
from codigos import Codigo
from vehiculos import Coche, Bicicleta, Camioneta, Motocicleta
from totareadme import readme

if __name__ == "__main__":
    readme(str(pathlib.Path().resolve()))
    eleccion = 0
    while eleccion != 6:
        eleccion = int(input('Bienvenido a la evaluacion del Tema 2. Elije un ejercicio para comenzar:\nEjercicio 1: Alumnos.\nEjercicio 2: Alumnos avanzado.\nEjercicio 3: Productos.\nEjercicio 4: Excepciones.\nEjercicio 5: Vehiculos.\nPara salir del programa (6).\nEleccion: '))
        os.system('cls')
        print('\n')
        if eleccion == 1:
            alumno = Alumno(input('Introduce el nombre del alumno: '), input('Introduce la nota del alumno: '))
        elif eleccion == 2:
            alumno = Alumno_str(input('Introduce el nombre del alumno: '), input('Introduce la nota del alumno: '))
            print(alumno)
        elif eleccion == 3:
            producto = Producto(input('Introduce el codigo del producto: '), input('Introduce el nombre del producto: '), input('Introduce el precio del producto: '), input('Introduce el tipo del producto: '))
            print(producto)
        elif eleccion == 4:
            codigo = Codigo(eleccion)
            codigo.iniciar()
        elif eleccion == 5:
            _input = 0
            while _input != 6:
                _input = input('Introduce el tipo de vehiculo que quieres crear:\n1. Coche.\n2. Bicicleta.\n3. Camioneta.\n4. Motocicleta.\n5. Contar ruedas\n6. Salir.\nEleccion: ')
                if _input == '1':
                    coche = Coche(input('Introduce el color del coche: '), 4, int(input('Introduce la velocidad maxima del coche: ')), int(input('Introduce la cilindrada del coche: ')))
                    print(coche)
                elif _input == '2':
                    bicicleta = Bicicleta(input('Introduce el color de la bicicleta: '), 2, input('Introduce el tipo de bicicleta (Urbana/Deportiva): '))
                    print(bicicleta)
                elif _input == '3':
                    camioneta = Camioneta(input('Introduce el color de la camioneta: '), 4, input('Introduce la velocidad maxima de la camioneta: '), input('Introduce la cilindrada del coche: '), input('Introduce la carga maxima de la camioneta: '))
                    print(camioneta)
                elif _input == '4':
                    motocicleta = Motocicleta(input('Introduce el color de la motocicleta: '), 2, input('Introduce el tipo de motocicleta (Urbana/Deportiva): ') , input('Introduce la velocidad maxima de la motocicleta: '), input('Introduce la cilindrada de la motocicleta: '))
                    print(motocicleta)
                elif _input == '5':
                    ruedas = input('Introduce el numero de ruedas: ')
                    Vehiculo.catalogar(int(ruedas))
                print('\n')