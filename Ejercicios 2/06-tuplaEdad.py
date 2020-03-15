# Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20.
# Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

tupla = []
contador = 0

for i in range(10):
    print("Ingrese la edad de la persona número ",i+1)
    tupla.append(int(input()))

for i in tupla:
    if i > 20:
        contador += 1

print("La cantidad de personas mayor a 20 es de: ",contador)