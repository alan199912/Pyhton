# Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.
# Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def es_bisiesto(year):
    if year % 4 == 0:
        print("El año ",year," es bisiesto")
    else:
        print("El año ",year," no es bisiesto")
year = int(input("Ingrese un año: "))

es_bisiesto(year)