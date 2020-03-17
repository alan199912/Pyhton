# Escribe un programa que pida dos palabras y diga si riman o no.
# Si coinciden las tres últimas letras tiene que decir que riman.
# Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra1 = palabra2 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese una segunda palabra: ")

if palabra1[-2:] == palabra2[-2:]:
    print("Las palabras "+palabra1+" y "+ palabra2+" riman")
else:
    print("Las palabras "+palabra1+" y "+ palabra2+" no riman")