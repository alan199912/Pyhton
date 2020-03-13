# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vocal(char):
    encontrada = True
    for letra in char:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            print(encontrada)
            break
        else:
            encontrada = False
            print(encontrada)
            break
        

letra = input("Ingrese una palabra: ")
vocal(letra)