# Samuel Gutiérrez Merino
# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y
# las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario
# cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas 
# hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.
# Crear un diccionario para almacenar nombres y notas de los alumnos
alumnos_notas_gutiérrez = {}
num_alumnos = int(input("Ingrese el número de alumnos: "))
for _ in range(num_alumnos):
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    if nombre_alumno in alumnos_notas_gutiérrez:
        print("Error: El nombre del alumno ya existe. Introduzca un nombre único.")
        continue
    notas_alumno = []
    while True:
        nota = float(input(f"Ingrese la nota del alumno {nombre_alumno} (introduzca un número negativo para terminar): "))
        if nota < 0:
            break
        notas_alumno.append(nota)
    alumnos_notas_gutiérrez[nombre_alumno] = notas_alumno
print("Lista de alumnos y su nota media:")
for nombre, notas in alumnos_notas_gutiérrez.items():
    nota_media = sum(notas) / len(notas) if notas else 0
    print(f"{nombre}: Notas = {notas}, Nota Media = {nota_media:.2f}")