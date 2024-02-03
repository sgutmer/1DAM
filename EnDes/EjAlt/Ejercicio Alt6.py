# Samuel Gutiérrez Merino
# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
cadena = str(input("Escribe algo: "))
mayus = any(letra.isupper () for letra in cadena)
if mayus==True:
    print("Hay al menos una mayúscula en el texto escrito")
else:
    print("No hay ninguna mayúscula en el texto escrito")