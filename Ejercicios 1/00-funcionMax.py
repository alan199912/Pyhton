# Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
# (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def maximo(num1, num2):

    if num1 > num2:
        return print("El numero ", num1 , "es mas grande que ", num2)
    else:
        return print("El numero ", num2 , "es mas grande que ", num1)

numero1 = int(input("ingrese un numero "))
numero2 = int(input("ingrese un segundo numero "))

maximo(numero1,numero2)