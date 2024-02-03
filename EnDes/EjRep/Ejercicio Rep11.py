# Samuel Gutiérrez Merino
# Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.
# Solicitar al usuario que ingrese un número
num_gutiérrez = int(input("Ingresa un número: "))
primo = True
if num_gutiérrez< 2:
    primo = False
else:
    for i in range(2, int(num_gutiérrez ** 0.5) + 1):
        if num_gutiérrez% i == 0:
            primo = False
if primo==True:
    print("El número es primo")
else:
    print("El número no es primo.")
