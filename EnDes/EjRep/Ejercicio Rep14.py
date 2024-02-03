# Samuel Gutiérrez Merino
# Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad.
# Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.
coche1_gutiérrez = 70
coche2_gutiérrez = 150
while coche1_gutiérrez!=coche2_gutiérrez:
    coche1_gutiérrez+=1
    coche2_gutiérrez-=1
punto_encuentro_gutiérrez=coche2_gutiérrez
print("Los coches se encontrarán en el kilómetro", punto_encuentro_gutiérrez)