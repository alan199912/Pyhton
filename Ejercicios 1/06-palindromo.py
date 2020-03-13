# Definir una función es_palindromo() que reconoce palíndromos
# (es decir, palabras que tienen el mismo aspecto escritas invertidas)
# ejemplo: es_palindromo ("radar") tendría que devolver True.

def palindromo(string):
    bandera = True
    invertida = string[::-1]
    
    if string == invertida:
        print(bandera)
    else:
        bandera = False
        print(bandera)

palabra = input("Ingrese un palindromo ")

palindromo(palabra)