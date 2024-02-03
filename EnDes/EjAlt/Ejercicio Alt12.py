# Samuel Gutiérrez Merino
# Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4,
# pero no si es divisible por 100, excepto que también sea divisible por 400.
año = int(input("Introduce un año: "))
if (año%4)==0 or (año%400)==0:
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")