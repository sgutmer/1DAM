# Samuel Gutiérrez Merino
# Introducir una cadena de caracteres e indicar si es un palíndromo.
# Una palabra palíndroma es aquella que se lee igual adelante que atrás.
cadena_gutiérrez = input("Introduce una cadena de caracteres para ver si es palíndroma o no: ")
cadena_progreso_gutiérrez = cadena_gutiérrez.replace(" ","")
cadena_final_gutiérrez = cadena_progreso_gutiérrez.lower()
cadena_inversa_gutiérrez = cadena_final_gutiérrez[::-1]
if cadena_final_gutiérrez == cadena_inversa_gutiérrez:
    print("El texto introducido es palíndromo")
else:
    print("El texto introducido no es palíndromo")