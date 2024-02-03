# Samuel Gutiérrez Merino
# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores),
# y posterior ordene los elementos de menor a mayor.
import random
lista_random_gutiérrez = []
i = 0
min_gutiérrez = 100
max_gutiérrez = 0
while i != 11:
    num_gutiérrez = random.randint(0,100)
    lista_random_gutiérrez.append(num_gutiérrez)
    i+=1
print("La lista desordenada es:", lista_random_gutiérrez)
lista_random_gutiérrez.sort()
print("Y tras ordenarla de menor a mayor queda así:", lista_random_gutiérrez)