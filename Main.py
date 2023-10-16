# Importando paquetes
from Producto import Producto
from Estudiante import Estudiante

# Instanciando clases
p1 = Producto(1, 'Leche Colanta Entera', 4000)
p2 = Producto(2, 'Arroz Roa', 2500)
p3 = Producto(3, 'Media de Aguardiente', 24000)

# Invocando el metodo __str__
print(p1)
print(p2)
print(p3)

# Modificando los objetos
p1.precio()
print(p1)