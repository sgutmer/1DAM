# Samuel Gutiérrez Merino
#  Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
# Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
# Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
# de la tabla anterior, y en la segunda los goles del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
equipos = []
resultados = []
for i in range(15):
    equipo_local = input(f"Ingrese el nombre del equipo local del partido {i + 1}: ")
    equipo_visitante = input(f"Ingrese el nombre del equipo visitante del partido {i + 1}: ")
    goles_local = int(input(f"Ingrese los goles del {equipo_local}: "))
    goles_visitante = int(input(f"Ingrese los goles del {equipo_visitante}: "))
    equipos.append([equipo_local, equipo_visitante])
    resultados.append([goles_local, goles_visitante])
print("Quiniela de la Jornada:")
for i in range(15):
    partido = f"{equipos[i][0]} vs {equipos[i][1]}"
    resultado = f"{resultados[i][0]} - {resultados[i][1]}"
    print(f"Partido {i + 1}: {partido}, Resultado: {resultado}")
