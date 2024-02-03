# Samuel Gutiérrez Merino
# Escribe un programa en python que lea el fichero json colores.json con datos de colores, deberá mostrar en la terminal todos los nombres de colores, sus códigos rgba y hexadecimal respectivamente.
import json
with open('colores.json') as archivo:
    datos = json.load(archivo)
for color_info in datos['colors']:
    nombre_gutierrez = color_info['color']
    rgba_gutierrez = color_info['code']['rgba']
    hexa_gutierrez = color_info['code']['hex']
    print(f"Color: {nombre_gutierrez}")
    print(f"Código RGBA: {rgba_gutierrez}")
    print(f"Código hexadecimal: {hexa_gutierrez}")
    print()