# Escribir una funcion sum() y una función multip() que sumen
# y multipliquen respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(array):
    contador = 0
    for lista in array:
        contador += lista
    print(contador)

def mult(array):
    contador = 1
    for lista in array:
        contador *= lista
    print(contador)

cantidad = int(input("ingresa la cantidad de numeros que quiera sumar: "))

arreglo = []

for i in range(cantidad):
    arreglo.append(int(input("Ingresa numeros: ")))
    
opcion = input("que desea hacer? \n multiplicar o sumar, ingrese por teclado ")

if opcion == "sumar":
    sum(arreglo)
elif opcion == "multiplicar":
    mult(arreglo)
else:
    print("ingrese bien los datos")
