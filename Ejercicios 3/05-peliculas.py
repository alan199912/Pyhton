# Este programa muestra primero el listado de categorías de películas y
# pide al usuario que introduzca el código de la categoría de la película y
# posterior a ello pide que el usuario introduzca el número de días de atraso,
# y así se muestra al final el total a pagar

peliculas = [
    [1, "Favoritos", 200, 50],
    [2, "Nuevos", 350, 100],
    [3, "Estrenos", 500, 350],
    [4, "Super Estrenos", 750, 400]
]

tienda = True
recargo = 0
precio_total = 0
compra = ""
peli_comprada = []
peli_recargo = []
contador = 0

while tienda == True:

    print("Elija la pelicula deseada:\n\n \tCategoria ---------- Precio ---------- Codigo ---------- Recargo/*dia")

    for i in peliculas:
        print("\t ",i[1]," ---------- ",i[2]," ---------- ",i[0]," ---------- ",i[3],"\t")

    cod_peli = int(input("\nIngrese el codigo que desee: "))

    if cod_peli >= 1 and cod_peli <=4:
        for i in peliculas:
            if cod_peli == i[0]:
                recargo = int(input("Introduzca el numero de dias de recargo: "))
                peli_recargo.append(recargo)
                precio_total += i[2]* recargo
                contador += 1
                peli_comprada.append(i[1])

                compra = input("Desea seguir comprando? \n 'si' si desea seguir comprando\n 'no' si desea terminar su compra: ")

                if compra == "no":
                    print("\n Su compra ha terminado \n ")

                    for i in range(contador):
                        print(peli_comprada[i]," con ",peli_recargo[i]," dias recargo ")

                    print("El total a pagar es de $",precio_total,"\n")
                    tienda = False
                elif compra == "si":
                    print("Continue comprando...\n")
                else:
                    print("La proxima vez precione 'si' o 'no'")
                    tienda = False
    else:
        print("Producto invalido")
        tienda = False