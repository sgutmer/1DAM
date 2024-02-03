# Samuel Gutiérrez Merino
# Pide al usuario dos números y muestra la “distancia” entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
num1 = float(input("Introduce el primer número: "));
num2 = float(input("Introduce el segunto número: "));
dist = abs(num2 - num1);
print(f"La distancia entre los dos números es de {dist}")