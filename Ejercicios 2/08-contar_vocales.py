# Crear una función contar_vocales(), que reciba una palabra y
# cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
# Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(word):
    word = word.lower()
    vocales = "aeiou"

    for i in vocales:
        contador = 0
        for j in word:
            if i == j:
                contador += 1
        print("Hay ",contador," vocal "+i)

palabra = input("Ingrese una palabra: ")

contar_vocales(palabra)