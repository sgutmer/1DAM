# Samuel Gutiérrez Merino
# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) 
# Al finalizar se mostrará los siguientes datos:
# Todos lo alumnos mayores de edad.
# Los alumnos mayores (los que tienen más edad)
lista_nombres_gutiérrez = []
lista_edades_gutiérrez = []
nombre_gutiérrez=""
edad_max=0
total=0
print("Introduce el nombre y la edad del alumno (Debe ser en distintas lineas de texto):")
while nombre_gutiérrez != "*":
    nombre_gutiérrez = input("")
    if nombre_gutiérrez == "*":
        break
    lista_nombres_gutiérrez.append(nombre_gutiérrez)
    edad_gutiérrez =  int(input(""))
    lista_edades_gutiérrez.append(edad_gutiérrez)
    total+=1
i = 0
j=0
print("Los alumnos mayores de edad son:")
while i<total:
    if lista_edades_gutiérrez[i]>=18:
        print (lista_nombres_gutiérrez[i])
    if lista_edades_gutiérrez[i]>edad_max:
        edad_max = lista_edades_gutiérrez[i]
        j = lista_edades_gutiérrez.index(edad_max)
    i+=1
print("Y el mayor alumno de la clase es:", lista_nombres_gutiérrez[j])