# Este programa muestra primero el listado de categorías de películas y
# pide al usuario que introduzca el código de la categoría de la película y
# posterior a ello pide que el usuario introduzca el número de días de atraso,
# y así se muestra al final el total a pagar

peliculas = [
    {
        "ID": 0,
        "categoria":"Favoritos",
        "precio": 200,
        "recargo": 50
    },
    {
        "ID": 1,
        "categoria":"Nuevos",
        "precio": 350,
        "recargo": 100
    },
    {
        "ID": 2,
        "categoria":"Estrenos",
        "precio": 500,
        "recargo": 350
    },
    {
        "ID": 3,
        "categoria":"Super estrenos",
        "precio": 750,
        "recargo": 400
    }
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
        print("\t ",i["categoria"]," ---------- ",i["precio"]," ---------- ",i["ID"]+1," ---------- ",i["recargo"],"\t")

    cod_peli = int(input("\nIngrese el codigo que desee: "))

    if cod_peli >= 1 and cod_peli <=4:
        for i in peliculas:
            if cod_peli == i["ID"]+1:
                recargo = int(input("Introduzca el numero de dias de recargo: "))
                peli_recargo.append(recargo)
                precio_total += i["precio"]* recargo
                contador += 1
                peli_comprada.append(i["categoria"])

                compra = input("Desea seguir comprando? \n 'si' si desea seguir comprando\n 'no' si desea terminar su compra: ")

                if compra == "no":
                    print("\n Su compra ha terminado \n ")

                    for i in range(contador):
                        print("elijio ",peli_comprada[i]," con ",peli_recargo[i]," dias recargo ")

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
