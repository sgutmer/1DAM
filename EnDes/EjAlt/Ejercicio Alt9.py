# Samuel Gutiérrez Merino
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
if num1>num2 and num1>num3:
    if num2>num3:
        print(f"El orden es {num1} (Nº1) // {num2} (Nº2) // {num3} (Nº3)")
    else:
        print(f"El orden es {num1} (Nº1) // {num3} (Nº3) // {num2} (Nº2)")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"El orden es {num2} (Nº2) // {num1} (Nº1) // {num3} (Nº3)")
    else:
        print(f"El orden es {num2} (Nº2) // {num3} (Nº3) // {num1} (Nº1)")
elif num3>num1 and num3>num2:
    if num1>num2:
        print(f"El orden es {num3} (Nº3) // {num1} (Nº1) // {num2} (Nº2)")
    else:
        print(f"El orden es {num3} (Nº3) // {num2} (Nº2) // {num1} (Nº1)")