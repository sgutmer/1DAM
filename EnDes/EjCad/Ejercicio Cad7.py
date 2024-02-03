# Samuel Gutiérrez Merino
# Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.
cadena_original_gutiérrez = input("Escribe una cadena de caracteres: ")
caracter_original_gutiérrez = input("Escribe el carácter a reemplazar: ")
validar_gutiérrez = len(caracter_original_gutiérrez)
while validar_gutiérrez!=1:
    caracter_original_gutiérrez = input("El carácter debe ser obligatoriamente un sólo carácter, por favor introduce UN CARÁCTER: ")
    validar_gutiérrez = len(caracter_original_gutiérrez)
caracter_nuevo_gutiérrez = input("Escribe el carácter que reemplazará al primero: ")
validar_gutiérrez = len(caracter_nuevo_gutiérrez)
while validar_gutiérrez!=1:
    carácter_nuevo_gutiérrez = input("El carácter debe ser obligatoriamente un sólo carácter, por favor introduce UN CARÁCTER: ")
    validar_gutiérrez = len(caracter_nuevo_gutiérrez)
cadena_modificada_gutiérrez = cadena_original_gutiérrez.replace(caracter_original_gutiérrez, caracter_nuevo_gutiérrez)
print("Tras sustituir los caracteres, la cadena ha quedado así:", cadena_modificada_gutiérrez)