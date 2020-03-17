# De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar.
# El programa determinará el total a pagar, como una factura.
# Una variante a este ejercicio que lo haría un poco más complejo
# sería dar la posibilidad de seguir ingresando diferentes códigos de productos con sus respectivas cantidades,
# y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras.

productos = [
    [1,"Camisa", 700],
    [2,"Cinturon", 200],
    [3,"Zapatos", 1500],
    [4,"Pantalon", 2000],
    [5,"Calcetines", 200],
    [6,"Faldas", 800],
    [7,"Gorras", 500],
    [8,"Sueter", 1700],
    [9,"Corbata", 900],
    [10,"Chaqueta", 7000]
]

precio_total = 0
unidades = 0
tienda = True
compra = ""
prod_comprado = []
unidades_compra = []
contador = 0

while tienda == True:

    print("Elija el producto deseado:\n\n \tProducto ------------- Codigo")

    for i in productos:
        print("\t",i[1]," ------------- ",i[0])

    codigo_prod = int(input("\nIntroduzca el codigo del producto: "))

    if codigo_prod >= 1 and codigo_prod <= 10:
        for i in productos:
            if codigo_prod == i[0]:
                print("\nEl precio del producto ",i[1]," es: $",i[2],"\n")
                unidades = int(input("Introduzca número de unidades deseadas: "))
                unidades_compra.append(unidades)
                precio_total += i[2]*unidades
                contador += 1
                prod_comprado.append(i[1])

                compra = input("Desea seguir comprando? \n 'si' si desea seguir comprando\n 'no' si desea terminar su compra: ")

                if compra == "no":
                    print("\nSu compra ha terminado \n")
                    # lista de cosas compradas
                    for i in range(contador):
                        print(unidades_compra[i]," de ",prod_comprado[i])

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
