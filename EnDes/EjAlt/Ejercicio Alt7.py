# Samuel Gutiérrez Merino
# Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
base = int(input("Introduce el valor de la base: "))
exp = int(input("Introduce el valor del exponente: "))
if exp==0:
    pot=1
    print(f"El resultado es {pot}")
elif exp>0:
    pot=base**exp
    print(f"El resultado es {pot}")
else:
    ex=0-exp
    pot=1/(base**ex)
    print(f"El resultado es {pot}")