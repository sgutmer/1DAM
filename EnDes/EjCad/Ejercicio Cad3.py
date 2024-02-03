# Samuel Gutiérrez Merino
# Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.
cadena_gutiérrez = input("Introduce una cadena de caracteres: ")
carácter_gutiérrez = input("introduce un sólo carácter: ")
validar_gutiérrez = len(carácter_gutiérrez)
while validar_gutiérrez!=1:
    carácter_gutiérrez = input("El carácter debe ser obligatoriamente un sólo carácter, por favor introduce UN CARÁCTER: ")
    validar_gutiérrez = len(carácter_gutiérrez)
cont_carácter_gutiérrez = cadena_gutiérrez.count(carácter_gutiérrez)
print("Hay", cont_carácter_gutiérrez, carácter_gutiérrez, "en la cadena")