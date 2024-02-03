# Samuel Gutiérrez Merino
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
# Muestra el contenido de la tabla en pantalla.
tabla_gutiérrez = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1]
]
for fila in tabla_gutiérrez:
    for num in fila:
        print(num, end="")
    print("")