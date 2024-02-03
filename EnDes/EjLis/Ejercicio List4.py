# Samuel Gutiérrez Merino
# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).
lista = []
cont_gutiérrez = 1
num_gutiérrez = 0
print("Introduce varios números. Para cerrar el programa, escribe un número negativo:")
while num_gutiérrez >= 0:
    num_gutiérrez = int(input())
    lista.append(num_gutiérrez)
    cont_gutiérrez+=1
    if num_gutiérrez < 0:
        break
lista.pop()
print("Has introducido estos números:")
for elem_gutiérrez in lista:
    print(elem_gutiérrez)