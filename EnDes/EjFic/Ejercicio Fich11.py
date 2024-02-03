# Samuel Gutierrez Merino
# Escribe un programa en python que lea el fichero gazpacho.json con datos su origen e ingredientes, a continuación deberá  crear otro fichero primerapellido_ingredientes.json con los todos los datos de sus ingredientes.
import json
with open('gazpacho.json') as archivo_gutierrez:
    datos = json.load(archivo_gutierrez)
ingredientes = []
for ingrediente in datos['ingredientes']:
    ingredientes.append({
        "nombre": ingrediente['nombre'],
        "cantidad": ingrediente['cantidad']
    })
with open('gutierrez_ingredientes.json', 'w') as archivo_nuevo_gutierrez:
    json.dump(ingredientes, archivo_nuevo_gutierrez, indent=2)
print("Se ha creado el archivo 'gutierrez_ingredientes.json' con los datos de los ingredientes.")