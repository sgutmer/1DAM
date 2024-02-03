# Samuel Gutiérrez Merino
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
print("Aquí tienes una lista con todos los números pares entre", num1, "y", num2,":")
while (num1<num2):
    num1 = num1+1
    par = num1%2
    if (par==0):
        print("·", num1)