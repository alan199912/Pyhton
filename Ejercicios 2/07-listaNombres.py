# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
# También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

cantidad = int(input("Ingrese la cantidad de la lista: "))

nombres = []
contador = 0
letra = ""


for i in range(cantidad):
    print(i," Ingrese nombre: ")
    nombres.append(input())

for i in nombres:
    if i[:1] == "a":
        contador += 1

print("Los nombres encontrados son: ", contador)

letra = input("Ingrese la letra que desea buscar: ")

for i in nombres:
    if i[:1] == letra:
        print("Nombres con la letra "+letra+": "+i)
