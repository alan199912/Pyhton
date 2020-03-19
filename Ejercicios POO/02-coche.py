# Crear una clase Coche, a traves de la cual se pueda conocer el color del
# coche, la marca, el modelo, el numero de caballos, el numero de puertas
# y la matrıcula. Crear el constructor del coche, ası como los metodos que
# considere necesarios.

class Auto:

    color = ""
    marca = ""
    modelo = ""
    caballosFuerza = 0

    def __init__(self, color, marca, modelo, caballosFuerza):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballosFuerza = caballosFuerza
    
    def __str__(self):
        return "El auto {self.marca} modelo {self.modelo} de color {self.color} con {self.caballosFuerza} caballos de fuerza".format(self=self)

# instancia

prueba_auto = Auto("Beige","Renault","Captur", 500) # ni idea los caballos de fuerza xd

prueba_auto2 = Auto("Negro","BMW","A4", 800) # ni idea los caballos de fuerza xd

prueba_auto3 = Auto("Blanco","Mercedes Benz","AMG GT", 1500) # ni idea los caballos de fuerza xd

print(prueba_auto)
print(prueba_auto2)
print(prueba_auto3)
