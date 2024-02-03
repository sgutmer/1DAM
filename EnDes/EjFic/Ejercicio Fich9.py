# Samuel Gutiérrez Merino
# Escribe un programa en python que lea el fichero json pedidos.json con datos de órdenes, deberá mostrar en la terminal todos las órdenes de pedidos que no se hayan entregado.
import json
with open('pedidos.json') as archivo:
    datos = json.load(archivo)
for orden_gutierrez in datos['ordenes']:
    if not orden_gutierrez['delivery']:
        print("Orden:")
        print(f"  Tamaño: {orden_gutierrez['tamano']}")
        print(f"  Precio: {orden_gutierrez['precio']}")
        print(f"  Toppings: {orden_gutierrez['toppings']}")
        print(f"  Queso Extra: {orden_gutierrez['queso_extra']}")
        print(f"  Entregado: {orden_gutierrez['delivery']}")
        cliente_gutierrez = orden_gutierrez['cliente']
        print(f"  Cliente:")
        print(f"    Nombre: {cliente_gutierrez['nombre']}")
        print(f"    Teléfono: {cliente_gutierrez['telefono'] if cliente_gutierrez['telefono'] else 'No proporcionado'}")
        print(f"    Correo: {cliente_gutierrez['correo'] if cliente_gutierrez['correo'] else 'No proporcionado'}")
        print()