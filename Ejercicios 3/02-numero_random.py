
# Ejercicio de números al azar
import random

flag = True
azar = random.randint(1, 100)
contador = 0

while flag == True:
    numero = int(input("Elija un número de 1 al 100: "))

    if numero < azar:
        print("Elija un número mayor  ")
        contador += 1
    elif numero > azar:
        print("Elija un número menor ")
        contador += 1
    else:
        contador += 1
        print("Felicitaciones usted elijio ",azar," es el ganador con ",contador," intentos")
        flag = False


