# Samuel Gutiérrez Merino
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
import random
i=1
j=0
lista_gutiérrez = []
print("La lista está formada por 10 valores aleatorios del 1 al 10, este es el valor de cada componente junto a su valor al cuadrado y al cubo:")
while i!=11:
    valor_gutiérrez = random.randint(1,10)
    lista_gutiérrez.append(valor_gutiérrez)
    print(lista_gutiérrez[j], lista_gutiérrez[j]**2, lista_gutiérrez[j]**3)
    i+=1
    j+=1