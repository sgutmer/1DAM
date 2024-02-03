# Samuel Gutiérrez Merino
# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
# Si introducimos otro número nos da un error.
día = int(input("Introduce un número del 1 al 7: "))
if día>=1 and día<=7:
    if día==1:
        print("El día Nº1 de la semana es el lunes")
    elif día==2:
        print("El día Nº2 de la semana es el martes")
    elif día==3:
        print("El día Nº3 de la semana es el miércoles")
    elif día==4:
        print("El día Nº4 de la semana es el jueves")
    elif día==5:
        print("El día Nº5 de la semana es el viernes")
    elif día==6:
        print("El día Nº6 de la semana es el sábado")
    elif día==7:
        print("El día Nº7 de la semana es el dominmgo")
else:
    print("ERROR: El número debe estar entre el 1 y el 7")