# Samuel Gutiérrez Merino
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
cantidad = int(input("Introduce la cantidad de números que deseas escribir: "))
mayor = 0
menor = 0
igual = 0
while (cantidad != 0):
    cantidad=cantidad-1
    num = int(input("Introduce un número: "))
    if num>0:
        mayor=mayor+1
    elif num<0:
        menor=menor+1
    elif num==0:
        igual=igual+1
print ("Has introducido", mayor, "números mayores que 0,", menor, "números menores que 0 y", igual, "números iguales que 0")