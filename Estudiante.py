# Importando la clase padre Persona
import Persona

# La clase estudiante hereda de persona
class Estudiante(Persona.Persona):
    def __init__(self, nombre, edad, nacionalidad, grado, promedio_acumulado):
        super().__init__(nombre, edad, nacionalidad)
        self.grado = grado
        self.promedio_acumulado = promedio_acumulado

    def __str__(self) -> str:
        # La coma , ayuda a acoplar los elementos
        return super().__str__() + str(", Me encuentro en el grado {self.grado} y mi promedio es: {self.promedio_acumulado}")