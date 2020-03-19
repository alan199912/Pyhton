# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad (puede tener decimales).
# El titular será obligatorio y la cantidad es opcional. Crea dos constructores que cumpla lo anterior.
# Crea sus métodos get, set y toString.
# Tendrá dos métodos especiales:
# ingresar(double cantidad): se ingresa una cantidad a la cuenta, 
#                               si la cantidad introducida es negativa, no se hará nada.
# retirar(double cantidad): se retira una cantidad a la cuenta,
#                           si restando la cantidad actual a la que nos pasan es negativa,
#                           la cantidad de la cuenta pasa a ser 0.

class Cuenta:

    # cosntructor 
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad


    # metodo string
    def __str__(self):
        return 'titular {self.titular} con {self.cantidad}'.format(self=self)
       
    # metodos
    def ingresar(self, cantidad):
        if cantidad < 0:
            print("No se puede ingresar saldo negativo")
        else:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if self.cantidad - cantidad < 0:
            self.cantidad = 0
        else:
            self.cantidad -= cantidad

# instancia

empleado = Cuenta("Alan", 500)

empleado.ingresar(5000)
empleado.retirar(500)
print(empleado)
