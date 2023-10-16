
# Definicion de la clase Producto
class Producto:
    # Metodo contructor -> el __atributo indica que el atributo es de ambito privado
    def __init__ (self, id: int, nombre: str, precio: float) -> None:
        # self.__atributo indica que python ocultará el atributo y no será público
        self.__id = id 
        self.__nombre = nombre
        self.__precio = precio
    # Metodo __str__ informacion del objeto
    def __str__ (self):
        return f'El producto con id: {self.__id}, es {self.__nombre} y su precio es de: {self.__precio}'
    # Encapsulamiento - Privacidad de Estado de Atributos - Métodos getters y setters
    @property #@property <=> getter
    def precio (self):
        print(f"Método Getter Invocado para el Atributo PRECIO del producto {self.__nombre}")
        return self.__precio
    # Metodos setter
    @precio.setter
    def precio (self, nuevo_precio):
        print('Método Setter Invocado para el Atributo PRECIO')
        if nuevo_precio <= 0:
            print('ERROR: El precio de un producto debe ser mayor que cero')
        else:
            self.__precio = nuevo_precio
            print(f'El nuevo precio del producto {self.__nombre}, es {nuevo_precio}')
    @precio.deleter # Permite eliminar el atributo de una instancia, una vez sea eliminado, no se podrá acceder a el
    def del_precio (self):
        print(f'El precio del producto {self.__nombre} fue eliminado correctamente')
        del self.__precio

