# Definir una función superposicion() que tome dos listas y
# devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado.

def superposicion(array1, array2):

    iguales = True
    contador = 0
    
    for i in array1:
        for j in array2:
            if i == j:
                contador += 1

    if contador > 0:
        print(iguales)
    else:
        iguales = False
        print(iguales)


lista1 = [1,2]
lista2 = [2,3]

superposicion(lista1, lista2)
