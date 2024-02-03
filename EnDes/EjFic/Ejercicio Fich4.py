# Samuel Gutiérrez Merino
# El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. 
# Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo al final del curso (convocatoria ordinaria). Realiza un programa que haga lo siguiente:
# Reciba el fichero de calificaciones.csv y devuelva una lista de listas, donde cada lista contiene la información de los exámenes y la asistencia de un alumno. Para ordenar la lista vamos a utilizar una función lambda:
# ordenados = sorted(csv_reader,key=lambda x:x[0])
# La función sorted recibe como parámetros la lista que deseas ordenar y el parámetro key es una función que le indica a sorted como debe ordenar, en este caso lambda x: x[0] le dice a sorted que como todos los elementos de la lista son listas escoja para comparar el primer valor de cada lista. Quizás es extraño ver lambda en el código pero es una abreviatura para funciones, si tienes dudas puede consultar documentaciones oficiales.
# Se deberá mostrar la lista ordenada en pantalla.
import csv
def calcular_nota_final(row):
    parcial1_gutierrez = float(row[3]) if row[3] else 0
    parcial2_gutierrez = float(row[4]) if row[4] else 0
    ordinario1_gutierrez = float(row[5]) if row[5] else 0
    ordinario2_gutierrez = float(row[6]) if row[6] else 0
    practicas_gutierrez = float(row[7]) if row[7] else 0
    ordinario_practicas_gutierrez = float(row[8]) if row[8] else 0
    if ordinario1_gutierrez or ordinario2_gutierrez or ordinario_practicas_gutierrez:
        return max(ordinario1_gutierrez, ordinario2_gutierrez, ordinario_practicas_gutierrez)
    else:
        return (parcial1_gutierrez + parcial2_gutierrez + practicas_gutierrez) / 3
with open('calificaciones.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    alumnos_gutierrez = []
    for row in csv_reader:
        nota_final_gutierrez = calcular_nota_final(row)
        alumnos_gutierrez.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], nota_final_gutierrez])
ordenados = sorted(alumnos_gutierrez, key=lambda x: x[0])
for alumno in ordenados:
    print(alumno[:-1]) 