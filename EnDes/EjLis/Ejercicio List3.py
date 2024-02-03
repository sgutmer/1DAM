# Samuel Gutiérrez Merino
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
lista_notas = []
i = 1
nota_max = 0
nota_min = 10
total = 0
print("Introduce las 5 notas de un alumno:")
while i!=6:
    nota = float(input())
    while nota < 0 or nota > 10:
        nota = float(input("La nota debe estar comprendida entre 0 y 10: "))
    lista_notas.append(nota)
    if nota > nota_max:
        nota_max = nota
    elif nota < nota_min:
        nota_min = nota
    total = total + nota
    i+=1
media = total/5
print("El alumno ha obtenido las siguientes notas:")
for elem_guitiérrez in lista_notas:
    print(elem_guitiérrez)
print("La media de sus notas es", media)
print("La nota más alta que ha obtenido es un", nota_max, "y la más baja un", nota_min)