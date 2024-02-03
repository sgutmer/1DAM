# Samuel Gutiérrez Merino
#  Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
#Las cantidades totales de cada articulo.
# La cantidad de artículos en la sucursal 2.
# La cantidad del articulo 3 en la sucursal 1.
# La recaudación total de cada sucursal.
# La recaudación total de la empresa.
# La sucursal de mayor recaudación.
precios = []
cantidades = []
for i in range(5):
    precio = float(input(f"Ingrese el precio del artículo {i + 1}: "))
    precios.append(precio)
for i in range(4):
    cantidades_sucursal = []
    for j in range(5):
        cantidad = int(input(f"Ingrese la cantidad del artículo {j + 1} vendida en la sucursal {i + 1}: "))
        cantidades_sucursal.append(cantidad)
    cantidades.append(cantidades_sucursal)
cantidades_totales = [sum(col) for col in zip(*cantidades)]
recaudacion_sucursal = [sum(p * c for p, c in zip(precios, col)) for col in cantidades]
recaudacion_total = sum(recaudacion_sucursal)
sucursal_max_recaudacion = recaudacion_sucursal.index(max(recaudacion_sucursal)) + 1
print("Resultados:")
print("Cantidades totales por artículo:")
for i in range(5):
    print(f"   Artículo {i + 1}: {cantidades_totales[i]} unidades")
print("Cantidad de artículos en la sucursal 2:")
print(f"   {cantidades[1]}")
print("Cantidad del artículo 3 en la sucursal 1:")
print(f"   {cantidades[0][2]} unidades")
print("Recaudación total por sucursal:")
for i in range(4):
    print(f"   Sucursal {i + 1}: {recaudacion_sucursal[i]}€")

print("Recaudación total de la empresa:")
print(f"{recaudacion_total}€")

print("Sucursal de mayor recaudación:")
print(f"   Sucursal {sucursal_max_recaudacion}")
