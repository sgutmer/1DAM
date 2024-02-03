# Samuel Gutiérrez Merino
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno,
# pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
lista1_gutiérrez = []
lista2_gutiérrez = []
lista3_gutiérrez = []
i=0
print("Introduce 5 valores para la primera lista:")
while i!=5:
    num_gutiérrez = int(input(""))
    lista1_gutiérrez.append(num_gutiérrez)
    i+=1
i=0
print("Introduce 5 valores para la segunda lista:")
while i!=5:
    num_gutiérrez = int(input(""))
    lista2_gutiérrez.append(num_gutiérrez)
    i+=1
lista3_gutiérrez=lista1_gutiérrez+lista2_gutiérrez
print("La lista resultante de unir las otras 2 es:", lista3_gutiérrez)