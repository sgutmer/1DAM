# Samuel Gutiérrez Merino
# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.
letra = 0
while (letra!=" "):
    letra = input("Introduce una letra (en minúsculas):  ")
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"): 
        print("VOCAL")
    elif letra == " ":
        break
    else:
        print("NO VOCAL")