# De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar.
# El programa determinará el total a pagar, como una factura.
# Una variante a este ejercicio que lo haría un poco más complejo
# sería dar la posibilidad de seguir ingresando diferentes códigos de productos con sus respectivas cantidades,
# y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras.

productos = [
    {
        "ID": 0,
        "producto": "Camisa",
        "precio": 700
    },
    {
        "ID": 1,
        "producto": "Cinturon",
        "precio": 200
    },
    {
        "ID": 2,
        "producto": "Zapatos",
        "precio": 1500
    },
    {
        "ID": 3,
        "producto": "Pantalon",
        "precio": 2000
    },
    {
        "ID": 4,
        "producto": "Calcetines",
        "precio": 200
    },
    {
        "ID": 5,
        "producto": "Faldas",
        "precio": 800
    },
    {
        "ID": 6,
        "producto": "Gorras",
        "precio": 500
    },
    {
        "ID": 7,
        "producto": "Sweater",
        "precio": 1700
    },
    {
        "ID": 8,
        "producto": "Corbata",
        "precio": 900
    },
    {
        "ID": 9,
        "producto": "Chaqueta",
        "precio": 7000
    }
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
        print("\t",i["producto"]," ------------- ",i["ID"]+1)

    codigo_prod = int(input("\nIntroduzca el codigo del producto: "))

    if codigo_prod >= 1 and codigo_prod <= 10:
        for i in productos:
            if codigo_prod == i["ID"]+1:
                print("\nEl precio del producto ",i["producto"]," es: $",i["precio"],"\n")
                unidades = int(input("Introduzca número de unidades deseadas: "))
                unidades_compra.append(unidades)
                precio_total += i["precio"]*unidades
                contador += 1
                prod_comprado.append(i["producto"])

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

