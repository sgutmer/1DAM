# Samuel Gutiérrez Merino
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
dia = (input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))
if (dia==6 and mes==11 and año==2023):
    print("Correcto, la fecha actual (a fecha de escribir esto) es el 06/11/2023")
else:
    print("Incorrecto, esa no es la fecha actual")