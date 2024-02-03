# Samuel Gutiérrez Merino
# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos
# guardados en el diccionario. Si la fruta no existe nos dará un error.
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
precios_gutiérrez = {
    "manzana": 0.4,
    "banana": 0.55,
    "uva": 1.6,
    "pera": 0.79
}
while True:
    fruta_gutiérrez = input("Escribe el nombre de la fruta (o ''salir'' si no hay nada más que hacer): ")
    if fruta_gutiérrez.lower() == "salir":
        break
    if fruta_gutiérrez in precios_gutiérrez:
        cantidad = int(input(f"Ingrese la cantidad de {fruta_gutiérrez} vendida: "))
        precio_total = precios_gutiérrez[fruta_gutiérrez] * cantidad
        print(f"El precio de {cantidad} {fruta_gutiérrez}(s) es: {precio_total:.2f}€")
    else:
        print("ERROR: La fruta ingresada no está registrada en la lista de precios.")
    respuesta = input("¿Desea hacer otra consulta? (s/n): ")
    if respuesta.lower() != "s":
        break
print("¡Que tenga un buen día!")