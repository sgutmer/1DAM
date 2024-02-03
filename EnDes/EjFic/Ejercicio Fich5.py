# Samuel Gutiérrez Merino
#Realice un programa que reciba de nuevo el fichero calificaciones.csv para añadir a cada lista de cada alumno un nuevo elemento, será la Nota Final del curso. El peso de cada parcial de teoría en la nota final es de un 30% 
# mientras que el peso del examen de prácticas es de un 40%. Si el alumno ha realizado alguna recuperación ordinaria, para el cálculo de la nota final se tomará esta como última nota del alumno. 
# Se deberá mostrar finalmente en la terminal la lista ordenada y será guardada en un fichero que se llamará calificacionfinal.csv
import csv
def calcular_nota_final(row):
    parcial1_gutierrez = float(row[3]) if row[3] else 0
    parcial2_gutierrez = float(row[4]) if row[4] else 0
    practicas_gutierrez = float(row[7]) if row[7] else 0
    ordinario_practicas_gutierrez = float(row[8]) if row[8] else 0
    if ordinario_practicas_gutierrez:
        return ordinario_practicas_gutierrez
    else:
        nota_teorica_gutierrez = 0.3 * ((parcial1_gutierrez + parcial2_gutierrez) / 2)
        nota_practicas_gutierrez = 0.4 * practicas_gutierrez
        return nota_teorica_gutierrez + nota_practicas_gutierrez
with open('calificaciones.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    alumnos_nota_final_gutierrez = []
    for row in csv_reader:
        nota_final_gutierrez = calcular_nota_final(row)
        alumnos_nota_final_gutierrez.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], nota_final_gutierrez])
ordenados = sorted(alumnos_nota_final_gutierrez, key=lambda x: x[0])
print("Lista ordenada con Nota Final:")
for alumno in ordenados:
    print(alumno)
with open('calificacionfinal.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Apellidos", "Nombre", "Asistencia", "Parcial1", "Parcial2", "Ordinario1", "Ordinario2", "Practicas", "OrdinarioPracticas", "NotaFinal"])
    csv_writer.writerows(ordenados)