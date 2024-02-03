# Samuel Gutiérrez Merino
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.
import random
# Lo siento, no conseguía que funcionase con tablas
lista1_gutiérrez = []
lista2_gutiérrez = []
lista3_gutiérrez = []
lista4_gutiérrez = []
lista5_gutiérrez = []
i = 0
while i<5:
    num_gutiérrez = random.randint(0,9)
    lista1_gutiérrez.append(num_gutiérrez)
    i+=1
i = 0
while i<5:
    num_gutiérrez = random.randint(0,9)
    lista2_gutiérrez.append(num_gutiérrez)
    i+=1
i = 0
while i<5:
    num_gutiérrez = random.randint(0,9)
    lista3_gutiérrez.append(num_gutiérrez)
    i+=1
i = 0
while i<5:
    num_gutiérrez = random.randint(0,9)
    lista4_gutiérrez.append(num_gutiérrez)
    i+=1
i = 0
while i<5:
    num_gutiérrez = random.randint(0,9)
    lista5_gutiérrez.append(num_gutiérrez)
    i+=1
for num1,num2,num3,num4,num5 in zip(lista1_gutiérrez,lista2_gutiérrez,lista3_gutiérrez,lista4_gutiérrez,lista5_gutiérrez):
    print(num1,num2,num3,num4,num5)
i = 1
while i<=5:
    fila_gutiérrez = lista1_gutiérrez[i-1]+lista2_gutiérrez[i-1]+lista3_gutiérrez[i-1]+lista4_gutiérrez[i-1]+lista5_gutiérrez[i-1]
    print("Suma de la fila",i,":",fila_gutiérrez)
    i+=1
columna1_gutiérrez = lista1_gutiérrez[0]+lista1_gutiérrez[1]+lista1_gutiérrez[2]+lista1_gutiérrez[3]+lista1_gutiérrez[4]
print("Suma de la columna 1:",columna1_gutiérrez)
columna2_gutiérrez = lista2_gutiérrez[0]+lista2_gutiérrez[1]+lista2_gutiérrez[2]+lista2_gutiérrez[3]+lista2_gutiérrez[4]
print("Suma de la columna 2:",columna2_gutiérrez)
columna3_gutiérrez = lista3_gutiérrez[0]+lista3_gutiérrez[1]+lista3_gutiérrez[2]+lista3_gutiérrez[3]+lista3_gutiérrez[4]
print("Suma de la columna 3:",columna3_gutiérrez)
columna4_gutiérrez = lista4_gutiérrez[0]+lista4_gutiérrez[1]+lista4_gutiérrez[2]+lista4_gutiérrez[3]+lista4_gutiérrez[4]
print("Suma de la columna 4:",columna4_gutiérrez)
columna5_gutiérrez = lista5_gutiérrez[0]+lista5_gutiérrez[1]+lista5_gutiérrez[2]+lista5_gutiérrez[3]+lista5_gutiérrez[4]
print("Suma de la columna 5:",columna5_gutiérrez)