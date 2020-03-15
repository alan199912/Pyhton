# Construir un pequeño programa que convierta números binarios en enteros.

binario = int(input("Ingrese un número binario: "))

binario = str(binario)

decimal = 0

exponente = len(binario) -1
print("exponente ",exponente)

for i in binario:
    print("i "+i)
    print("exp ",exponente)
    decimal  += ( int(i)*2 **exponente )
    exponente = exponente -1

print(decimal)