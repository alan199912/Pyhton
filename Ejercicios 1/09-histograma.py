# Definir un histograma procedimiento() que tome una lista de números enteros
# e imprima un histograma en la pantalla.
# Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******

def procedimiento(array):
    codigo = "*"
    for i in array:
        print(i*codigo)
    

lista = [4, 9, 7]

procedimiento(lista)