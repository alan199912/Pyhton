# Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(array):
    mayor = 0
    for i in array:
        if( mayor < i ):
            mayor = i
    print("El número mayor es el: ",mayor)

cantidad = int(input("Ingrese la cantidad de la lista: "))

lista = []

for i in range(cantidad):
    lista.append(int(input("Ingrese numeros a la lista: ")))

max_in_list(lista)