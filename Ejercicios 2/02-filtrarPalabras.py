# Escribir una función filtrar_palabras()
# que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(array, num):
    for i in array:
        if len(i) > num:
            print(i)

cantidad = int(input("Ingrese la cantidad de la lista: "))

lista = []

for i in range(cantidad):
    lista.append(input("Ingrese palabras a la lista: "))

cant_palabras = int(input("Ingrese número limite de las palabras: "))

filtrar_palabras(lista, cant_palabras)