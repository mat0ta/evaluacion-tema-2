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
    def calificacion(self):
        if self.nota < 5:
            return 'Suspenso'
        else:
            return 'Aprobado'
    def __str__(self):
        return 'El alumno {} con una calificacion de {} esta {}'.format(self.nombre, self.nota, self.calificacion())

if __name__ == "__main__":
    alumno = Alumno('Juan', 5)
    print(alumno)