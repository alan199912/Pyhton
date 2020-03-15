# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.

current_year = int(input("Ingrese el año en curso: "))

people = []
age = []

for i in range(3):
    people.append(input("Ingresa nombre: "))
    for j in range(1):
        age.append(int(input("Ingresa año de nacimiento: ")))

for i in people:
    for j in age:
        if age.index(j) == people.index(i):
            calculo = current_year - j
            print("nombre "+i+" año de nacimiento ",j," cumplen ",calculo," este año")
