# Definicion de la clase Conductor
class Conductor:
    # Atributos
    nombre = ""
    edad = 0
    licencia = ""

    # Metodos
        # Metodo constructor o inicializador
    def __init__(self, nombre, edad, licencia):
        self.nombre = nombre
        self.edad = edad
        self.licencia = licencia

    # Este metodo permite brindar una descripcion informal a un objeto cuando se invoca una funcion print()
    def __str__ (self):
        return f"¡Hola! mi nombre es {self.nombre}, tengo {self.edad} años y mi licencia es del tipo {self.licencia}"

    # Clase vacia -> pass


# Instanciamiento de objetos
conductor_1 = Conductor("THOMAS VANEGAS", 19, "A2")
conductor_2 = Conductor("PIEDAD ACEVEDO", 56, "B1")

# Invocando metodos de los objetos
# print(conductor_1.presentar()) -> sin usar el método __str__

# Haciendo uso del metodo __str__
print(conductor_1)
print(conductor_2)