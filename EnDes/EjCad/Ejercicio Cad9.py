# Samuel Gutiérrez Merino
# Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
cadena_gutiérrez = input("Introduce la primera cadena de caracteres: ")
subcadena_gutiérrez = input("Introduce la segunda cadena de caracteres: ")
if cadena_gutiérrez.find(subcadena_gutiérrez)>=0:
    print("Se ha encontrado la primera cadena dentro de la segunda")
else: 
    print("No se ha encontrado la primera cadena")