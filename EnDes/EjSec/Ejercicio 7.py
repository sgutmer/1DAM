# Samuel Gutiérrez Merino
# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla
# a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
min = int(input("Ingrese la cantidad de minutos: "))
h = min // 60
min_r = min % 60
print(f"{min} minutos equivalen a {h} horas y {min_r} minutos.")