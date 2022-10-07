<h1 align="center">EVALUACION-TEMA-2</h1>

En este [repositorio](https://github.com/mat0ta/evaluacion-tema-2) quedan resueltos los ejercicios la tarea de esta semana. Puedes encontrar otros proyectos y tareas en mi perfil de GitHub: [mat0ta](https://github.com/mat0ta).

<h2>Ejercicio 1</h2>

Crea una clase llamada Alumno que tenga los atributos nombre y nota. Crea el constructor de la clase. A�adir en el constructor un print para informar de que el alumno se ha creado con �xito. Crear un m�todo llamado calificacion que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota

El c�digo empleado para crear dicho algoritmo es el siguiente:

```py

class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        try:
            self.nota = float(nota)
        except ValueError:
            print('Nota inválida. Se asignará 0')
            self.nota = 0
        print('Alumno creado con éxito.\n Nombre: {}\n Nota: {}'.format(self.nombre, self.nota))
        self.calificacion()
    def calificacion(self):
        if self.nota < 5:
            print('El alumno {} con una calificacion de {} esta Suspenso'.format(self.nombre, self.nota))
        else:
            print('El alumno {} con una calificacion de {} esta Aprobado'.format(self.nombre, self.nota))

```

<h2>Ejercicio 2</h2>

Copia el ejercicio anterior y realicemos una modificaci�n: Junto al m�todo init y calificacion, vamos a crear otro m�todo especial de Python, el m�todo str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato: def __str__(self): return "Lo que quiero mostrar" Este m�todo nos sirve para imprimir por pantalla la informaci�n de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutar� el contenido del m�todo str (el m�todo str lo que tiene que hacer es maquetar la informaci�n que desea en un string).

El c�digo empleado para crear dicho algoritmo es el siguiente:

```py

class Alumno_str():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        try:
            self.nota = float(nota)
        except ValueError:
            print('Nota inválida. Se asignará 0')
            self.nota = 0
        print('Alumno creado con éxito.\n Nombre: {}\n Nota: {}'.format(self.nombre, self.nota))
    def calificacion(self):
        if self.nota < 5:
            return 'Suspenso'
        else:
            return 'Aprobado'
    def __str__(self):
        return 'El alumno {} con una calificacion de {} esta {}'.format(self.nombre, self.nota, self.calificacion())

```

<h2>Ejercicio 3</h2>

Crea una clase llamada Producto que tenga los atributos codigo, nombre, precio y tipo. Crea el constructor de la clase. A�adir en el constructor un print para informar de que el producto se ha creado con �xito. Crea el m�todo __str__ para visualizar por pantalla la informaci�n de los productos.

El c�digo empleado para crear dicho algoritmo es el siguiente:

```py

class Producto():
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print('Producto creado con éxito.')
    def __str__(self):
        return 'Nombre: {}\nCodigo: {}\nPrecio {} €\nTipo: {}'.format(self.nombre, self.codigo, self.precio, self.tipo)

```

<h2>Ejercicio 4</h2>

Identificar los errores en los siguiente bloques de c�digo y evaluarlos con excepciones especificas para evitar errores no controlados en nuestros programas. A�ade m mensajes explicativos para el usuario. Nota: Se tienen que evaluar excepciones concretas, no hacer referencia a Exception sin m�s.

El c�digo empleado para crear dicho algoritmo es el siguiente:

```py

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

```

<h2>Ejercicio 5</h2>

En este ejercicio vas a trabajar el concepto de herencia un poco m�s en profundidad, aprovechando para introducir un nuevo concepto muy importante que te facilitar� la vida. Hasta ahora sabemos que una clase heredada puede f�cilmente extender algunas funcionalidades, simplemente a�adiendo nuevos atributos y m�todos, o sobreescribiendo los ya existentes. Utilizando esta nueva t�cnica extiende la clase Vehiculo y realiza la siguiente implementaci�n: Crea al menos un objeto de cada subclase y a��delos a una lista llamada vehiculos. Realiza una funci�n llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos. Modifica la funci�n catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre �nicamente los que su n�mero de ruedas concuerde con el valor del argumento. Tambi�n debe mostrar un mensaje "Se han encontrado {} veh�culos con {} ruedas:" �nicamente si se env�a el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.

El c�digo empleado para crear dicho algoritmo es el siguiente:

```py

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
        return super().__str__() + ", Velocidad: {} km/h, Cilindrada: {} cc".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        if tipo.lower() == "urbana" or tipo.lower() == "deportiva":
            super().__init__(color, ruedas)
            self.tipo = tipo
        else:
            self.nottipo = tipo
    def __str__(self):
        try:
            return super().__str__() + ", Tipo: {}".format(self.tipo)
        except AttributeError:
            return "Tipo de bicicleta no válido (" + self.nottipo + ")"

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return super().__str__() + ", Carga: {} kg".format(self.carga)
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        if tipo.lower() == "urbana" or tipo.lower() == "deportiva":
            super().__init__(color, ruedas, tipo)
            self.velocidad = velocidad
            self.cilindrada = cilindrada
        else:
            self.nottipo = tipo
    def __str__(self):
        try:
            return super().__str__() + ", Velocidad: {} km/h, Cilindrada: {} cc".format(self.velocidad, self.cilindrada)
        except AttributeError:
            return "Tipo de motocicleta no válido (" + self.nottipo + ")"

```

