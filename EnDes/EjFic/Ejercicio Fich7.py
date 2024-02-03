# Samuel Gutiérrez Merino
# El fichero cotizaciones.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), 
# Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).
# Construir un programa que reciba el fichero de cotizaciones , devuelva un diccionario y lo imprima en la terminal con el mismo formato que el fichero. 
# A continuación se deberá crear una lista de diccionarios con el nombre de las columnas medibles, su máximo, su mínimo y su media aritmética. Esta lista se deberá guardar en un fichero llamado ejercicio7_primerapellido en formato csv.
import csv
def cotizaciones_gutierrez(nombre_archivo):
    datos = {}
    try:
        with open(nombre_archivo, newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                datos[row['Nombre']] = {
                    'Final': float(row['Final']),
                    'Máximo': float(row['Máximo']),
                    'Mínimo': float(row['Mínimo']),
                    'Volumen': float(row['Volumen']),
                    'Efectivo': float(row['Efectivo'])
                }
        return datos
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no existe.')
        return None
def generar_estadisticas(datos):
    estadisticas = []
    columnas_medibles = ['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']
    for columna in columnas_medibles:
        valores_gutierrez = [datos[empresa][columna] for empresa in datos]
        maximo = max(valores_gutierrez)
        minimo = min(valores_gutierrez)
        media = sum(valores_gutierrez) / len(valores_gutierrez)
        estadistica_columna = {
            'Columna': columna,
            'Máximo': maximo,
            'Mínimo': minimo,
            'Media': media
        }
        estadisticas.append(estadistica_columna)
    return estadisticas
def guardar_estadisticas(estadisticas_gutierrez):
    nombre_archivo = 'ejercicio7_gutierrez.csv'
    with open(nombre_archivo, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Columna', 'Máximo', 'Mínimo', 'Media'])
        for estadistica in estadisticas_gutierrez:
            csv_writer.writerow([estadistica['Columna'], estadistica['Máximo'], estadistica['Mínimo'], estadistica['Media']])

    print(f'Estadísticas guardadas en {nombre_archivo}')
datos_cotizaciones_gutierrez = cotizaciones_gutierrez('cotizaciones.csv')
if datos_cotizaciones_gutierrez:
    estadisticas_gutierrez = generar_estadisticas(datos_cotizaciones_gutierrez)
    guardar_estadisticas(estadisticas_gutierrez)