# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(array):
    mayor = 0
    indice = 0
    for i in array:
        if mayor < len(i):
            mayor = len(i)
            indice = array.index(i)
    print("La palabra mas larga es: "+array[indice]+" con ", mayor, " palabras")

cantidad = int(input("Ingrese cantidad de la lista: "))

lista = []

for i in range(cantidad):
    lista.append(input("Ingrese palabras: "))

mas_larga(lista)
