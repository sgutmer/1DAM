# Samuel Gutiérrez Merino
# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
cara = int(input("Introduce el número presente en la cara del dado: "))
if (cara<6 and cara>1):
    if (cara==1):
        print("La cara opuesta es el [seis]")
    elif (cara==6):
        print("La cara opuesta es el [uno]")
    elif (cara==2):
        print("La cara opuesta es el [cinco]")
    elif (cara==5):
        print("La cara opuesta es el [dos]")
    elif (cara==3):
        print("La cara opuesta es el [cuatro]")
    elif (cara==4):
        print("La cara opuesta es el [tres]")
else:
    print("ERROR: Número incorrecto ;-;")