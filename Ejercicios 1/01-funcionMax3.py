# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def maximo(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        return print("El primer numero ", num1 ," es mayor a ", num2," y a ",num3)
    elif num2 > num1 and num2 > num3:
        return print("El segundo numero ", num2 ," es mayor a ", num1," y a ",num3)
    else:
        return print("El tercer numero ", num3 ," es mayor a ", num1," y a ",num2)

numero1 = int( input( "Ingrese el primer numero: " ) )
numero2 = int( input( "Ingrese el segundo numero: " ) )
numero3 = int( input( "Ingrese el tercer numero: " ) )

maximo(numero1, numero2, numero3)
