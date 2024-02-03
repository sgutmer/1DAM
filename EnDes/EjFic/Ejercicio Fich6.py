# Samuel Gutiérrez Merino
# Realice un programa que reciba de nuevo el fichero calificacionfinal.csv para  generar dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. 
# Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75% y la nota final mayor o igual que 5. Se deberá guardar las dos listas en dos ficheros distintos con los nombres aprobados.csv y suspensos.csv.
import csv
def aprobar_alumno_gutierrez(row):
    asistencia_gutierrez = float(row[2].strip('%'))
    nota_final_gutierrez = float(row[9])
    if asistencia_gutierrez >= 75 and nota_final_gutierrez >= 5:
        return True
    else:
        return False
with open('calificacionfinal.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    aprobados_gutierrez = []
    suspendidos_gutierrez = []
    for row in csv_reader:
        if aprobar_alumno_gutierrez(row):
            aprobados_gutierrez.append(row)
        else:
            suspendidos_gutierrez.append(row)
with open('aprobados.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Apellidos", "Nombre", "Asistencia", "Parcial1", "Parcial2", "Ordinario1", "Ordinario2", "Practicas", "OrdinarioPracticas", "NotaFinal"])
    csv_writer.writerows(aprobados_gutierrez)
with open('suspendidos.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Apellidos", "Nombre", "Asistencia", "Parcial1", "Parcial2", "Ordinario1", "Ordinario2", "Practicas", "OrdinarioPracticas", "NotaFinal"])
    csv_writer.writerows(suspendidos_gutierrez)
print("Listas de aprobados y suspendidos generadas y guardadas en aprobados.csv y suspendidos.csv respectivamente.")