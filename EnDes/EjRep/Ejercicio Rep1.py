# Samuel Gutiérrez Merino
# Crea una aplicación que pida un número y calcule su factorial 
numero = int(input("Introduce un número: "))
i = 1
factorial = numero
while i!=numero:
    factorial = factorial*i
    i = i+1
print("El factorial de",numero,"es",factorial)