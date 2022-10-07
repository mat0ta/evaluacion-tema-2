import os
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.absolute()))
from alumnos import *
from alumnos_str import *
from productos import *
from codigos import *
from vehiculos import *

if __name__ == "__main__":
    eleccion = 0
    while eleccion != 6:
        eleccion = int(input('Bienvenido a la evaluacion del Tema 2. Elije un ejercicio para comenzar:\nEjercicio 1: Alumnos.\nEjercicio 2: Alumnos avanzado.\nEjercicio 3: Productos.\nEjercicio 4: Excepciones.\nEjercicio 5: Vehiculos.\nPara salir del programa (6).'))
        os.system('cls')
        if eleccion == 1:
            alumno = Alumno('Juan', 5)
            print(alumno)
        elif eleccion == 2:
            alumno = Alumno_str('Juan', 5)
            print(alumno)
        elif eleccion == 3:
            producto = Producto('Leche', 1.5, 2)
            print(producto)
        elif eleccion == 4:
            codigo = Codigo(eleccion)
            codigo.iniciar()
        elif eleccion == 5:
            coche = Coche("Rojo", 4, 210, 2500)
            print(coche)