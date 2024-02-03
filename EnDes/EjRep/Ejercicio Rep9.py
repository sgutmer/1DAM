# Samuel Gutiérrez Merino
# Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
base = float(input("Introduce el valor de la base: "))
exponente = int(input("Introduce el valor del exponente: "))
potencia = base
while (exponente>1):
    exponente = exponente-1
    potencia = potencia*base
print(f"La potencia de {base} es {potencia}")