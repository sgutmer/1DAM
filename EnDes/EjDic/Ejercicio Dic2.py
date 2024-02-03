# Samuel Gutiérrez Merino
# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
cadena_gutiérrez = input("Escribe una cadena de caracteres: ")
aparecer_gutiérrez = {}
for caracter in cadena_gutiérrez:
    if caracter in aparecer_gutiérrez:
        aparecer_gutiérrez[caracter] += 1
    else:
        aparecer_gutiérrez[caracter] = 1
print("En la cadena",cadena_gutiérrez,", este es el número de veces que aparece cada carácter:")
print(aparecer_gutiérrez)