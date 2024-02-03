# Samuel Gutiérrez Merino
# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
# Ejemplo, si se introduce 23 que muestre 32.
num = int(input("Ingrese un número de dos cifras: "));
ud = num % 10;
dec = num // 10;
numinv = ud*10 + dec;
print("El número invertido es", numinv)