# Samuel Gutiérrez Merino
# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, 
# ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque,
# considerando lo siguiente: si es de tipo A,
# se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. 
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. 
# Realice un algoritmo para determinar la ganancia obtenida.

tipo = input("Introduce el tipo de la uva (A o B): ")
tamaño = input("Introduce el tamaño de la uva (1 o 2): ")
precio = float(input("Introduce el precio inicial por kilo de las uvas: "))
cantidad = float(input("Introduce los kilos de uvas entregados: "))
descuento = 0
if tipo == "A":
    if tamaño == 1:
        descuento = 0.20  
    elif tamaño == 2:
        descuento = 0.30 
elif tipo == "B":
    if tamaño == 1:
        descuento = -0.30
    elif tamaño == 2:
        descuento = -0.50 
ganancia = (precio - descuento) * cantidad
print(f"La ganancia obtenida por el es de {ganancia}€")
