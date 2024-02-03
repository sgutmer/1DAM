# Samuel Gutiérrez Merino
# Escribe un programa en python que lea el fichero json libreria.json con datos de nuestra librería, recibe por teclado un límite inferior y superior para el precio y muestre en la terminal
# todos los libros cuyo precio esta en ese intervalo.
import json

def filtrar_libros_por_precio(json_data, precio_inferior, precio_superior):
    try:
        # Cargar el contenido del archivo JSON
        with open(json_data, 'r') as file:
            data = json.load(file)

        # Obtener la lista de libros
        books = data['bookstore']['book']

        # Filtrar los libros por precio
        libros_filtrados = [
            libro for libro in books
            if float(libro['price']) >= precio_inferior and float(libro['price']) <= precio_superior
        ]

        # Mostrar los libros filtrados
        print(f"Libros con precio entre {precio_inferior} y {precio_superior}:")
        for libro in libros_filtrados:
            print(f"Titulo: {libro['title']['__text']}, Autor: {libro['author']}, Precio: {libro['price']}")

    except FileNotFoundError:
        print(f"El archivo {json_data} no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {json_data}")
    except ValueError:
        print("Error: Asegúrate de ingresar valores numéricos para el rango de precios.")

# Solicitar al usuario los límites de precio
precio_inferior = float(input("Ingrese el precio inferior: "))
precio_superior = float(input("Ingrese el precio superior: "))

# Llamar a la función con el nombre del archivo JSON y los límites de precio
filtrar_libros_por_precio("libreria.json", precio_inferior, precio_superior)
