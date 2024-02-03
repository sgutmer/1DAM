# Samuel Gutiérrez Merino
# Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.
cadena_gutiérrez = input("Introduce la primera cadena de caracteres: ")
subcadena_gutiérrez = input("Introduce la segunda cadena de caracteres: ")
validación_gutiérrez = cadena_gutiérrez.startswith(subcadena_gutiérrez)
if validación_gutiérrez==True:
    print("Se ha encontrado la primera cadena al inicio de la segunda")
else: 
    print("No se ha encontrado al inicio de la primera cadena")