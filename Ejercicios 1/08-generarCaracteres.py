# Definir una función generar_n_caracteres() que tome un entero n y
#  devuelva el caracter multiplicado por n. 
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generear_caracteres(num, caracter):
    agregado = ""

    for i in range(num):
        agregado += caracter

    print(agregado)

generar = int(input("Cuantas veces quiere generar el caracter? "))
caracter = input("Que caracter quiere usar? ")

char = len(caracter)

if char == 1:
    generear_caracteres(generar, caracter)
else:
    print("Solo se puede utilizar un solo caracter")