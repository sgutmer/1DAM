#Samuel Gutiérrez Merino
# Escribe un programa en python que lea el fichero json libreria.json con datos de nuestra librería y muestre en la terminal cuántos libros hay en la librería
import json
def contar_libros(datos_libros):
    try:
        with open('libreria.json', 'r') as archivo_gutierrez:
            datos = json.load(archivo_gutierrez)
        libros = datos['bookstore']['book']
        num_libros = len(libros)
        print(f"La librería tiene {num_libros} libros.")
    except FileNotFoundError:
        print(f"El archivo {datos_libros} no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {datos_libros}")
contar_libros("libreria.json")
