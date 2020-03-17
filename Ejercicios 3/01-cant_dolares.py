# Has un programa que pida al usuario una cantidad de dolares,
# una tasa de interés y un numero de años.
# Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años
# si cada año se aplica la tasa de interés introducida.


dolares = float(input("Ingrese una cantidad de dolares: "))
interes = float(input("Ingrese tasa de interes: "))
year = int(input("Ingrese una año estimado: "))

tasa = dolares * (1 + interes/100)**year

print("La tasa de interes es de ", tasa)