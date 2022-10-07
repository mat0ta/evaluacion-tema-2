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