# Samuel Gutiérrez Merino
# Escribe un programa en python que lea el fichero json pedidos.json con datos de ordenes, a continuación deberá crear otro fichero primerapellido_clientes.json con los todos los datos de los clientes.
import json
with open('pedidos.json') as file:
    datos = json.load(file)
datos_cliente = []
for orden in datos['ordenes']:
    cliente_gutierrez = orden['cliente']
    datos_cliente.append({
        "nombre": cliente_gutierrez['nombre'],
        "telefono": cliente_gutierrez['telefono'] if cliente_gutierrez['telefono'] else None,
        "correo": cliente_gutierrez['correo'] if cliente_gutierrez['correo'] else None
    })
with open('gutierrez_clientes.json', 'w') as archivo_nuevo_gutierrez:
    json.dump(datos_cliente, archivo_nuevo_gutierrez, indent=2)
print("Se ha creado el archivo 'gutierrez_clientes.json' con los datos de los clientes.")
