
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def __str__(self) -> str:
        return f'Mi nombre es {self.nombre}, tengo {self.edad} y soy de {self.nacionalidad}'
