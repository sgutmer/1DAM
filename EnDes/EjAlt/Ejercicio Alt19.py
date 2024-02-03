# Samuel Gutiérrez Merino
# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
mes = int(input("Introduce un número del 1 al 12: "))
if mes>=1 and mes<=12:
    if mes==1:
        print("El mes Nº1 del año es Enero")
        print("Enero tiene 31 días")
    elif mes==2:
        print("El mes Nº2 del año es Febrero")    
        print("Febrero tiene 28 o 29 días, dependiendo si el año es bisiesto o no")
    elif mes==3:
        print("El mes Nº3 del año es Marzo")
        print("Marzo tiene 31 días")
    elif mes==4:
        print("El mes Nº4 del año es Abril")
        print("Abril tiene 30 días")
    elif mes==5:
        print("El mes Nº5 del año es Mayo")
        print("Mayo tiene 31 días")
    elif mes==6:
        print("El mes Nº6 del año es Junio")
        print("Junio tiene 30 días")
    elif mes==7:
        print("El mes Nº7 del año es Julio")
        print("Julio tiene 31 días")
    elif mes==8:
        print("El mes Nº8 del año es Agosto")
        print("Agosto tiene 31 días")
    elif mes==9:
        print("El mes Nº9 del año es Septiembre")
        print("Septiembre tiene 30 días")
    elif mes==10:
        print("El mes Nº10 del año es Octubre")
        print("Octubre tiene 31 días")
    elif mes==11:
        print("El mes Nº11 del año es Noviembre")
        print("Noviembre tiene 30 días")
    elif mes==12:
        print("El mes Nº12 del año es Diciembre")
        print("Diciembre tiene 31 días")
else:
    print("ERROR: El número debe estar entre el 1 y el 7")