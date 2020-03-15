# Escribir un programa que le diga al usuario que ingrese una cadena.
# El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

string = input("Ingrese una cadena de texto: ")

contador = 0
for i in string:
    if i == i.upper():
        contador += 1

print("La palabra "+ string +" tiene ", contador," mayúsculas")