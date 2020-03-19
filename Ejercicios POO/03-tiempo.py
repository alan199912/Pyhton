# Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda
# ser construıda indicando los tres atributos, solo la hora y minuto o solo
# la hora. Crear ademas los metodos necesarios para modificar la hora en
# cualquier momento de forma manual. Mantenga la integridad de los datos
# en todo momento.
# Crear una clase PruebaTiempo que prueba una hora concreta y la modifique a su gusto mostrandola por pantalla.

class Tiempo:
    horas = ""
    minutos = ""
    segundos = ""

    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
    
    def __str__(self):
        return "Hora {self.horas}: Minutos {self.minutos}: Segundos {self.segundos}".format(self=self)

# instancia
import datetime

tiempo = datetime.datetime.now()

time = Tiempo(tiempo.strftime("%H"), tiempo.strftime("%M"), tiempo.strftime("%S"))

print(time)