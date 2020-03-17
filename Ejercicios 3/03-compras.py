# Este programa pide primeramente la cantidad total de compras de una persona.
# Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción.
# Pero si la persona ingresa una cantidad en compras igual o superior a $1500.00,
# el programa genera de forma aleatoria un número entero del cero al cinco.
# Cada número corresponderá a un color diferente de cinco colores de bolas que
# hay para determinar el descuento que el cliente recibirá como premio.
# Si la bola aleatoria es color blanco, no hay descuento,
# pero si es uno de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla
# que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario,
# de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.

import random
import time

cant_total = int(input("Ingrese cantidad total de compra: "))
bolas = ["Blanco", "Verde", "Rojo", "Azul", "Amarillo", "Negro"]
bola_azar = random.choice(bolas)
promo_total = 0

if cant_total >= 1500:
    print("Usted aplica a la promocion")
    print("Girando el bolillero...")
    time.sleep(3)

    for i in bolas:
        if i == bola_azar:
            print("Salio la bola numero: ", bolas.index(i))
            if bolas.index(i) == 0:
                print("Usted no tiene promocion, intente con otra compra.")
            else:
                promocion = [5, 10, 20, 50, 75]
                promo_azar = random.choice(promocion)
                print("Usted se gano una promocion del ",promo_azar," %")
                promo_total = (cant_total - ((cant_total * promo_azar) / 100))
                print("Pago total con promocion: ",promo_total)