# Samuel Gutiérrez Merino
# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas 
# que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
salario_base = float(input("Ingresa tu salario base: "))
venta1 = float(input("Ingresa lo que has ganado en la primera venta: "))
venta2 = float(input("Ingresa lo que has ganado en la segunda venta: "))
venta3 = float(input("Ingresa lo que has ganado en la tercera venta: "))
com1 = venta1 * 0.10
com2 = venta2 * 0.10
com3 = venta3 * 0.10
total = com1 + com2 + com3
salario = salario_base + total
print(f"Recibirás {total}€ por las comisiones este mes.")
print(f"Tu salario total será de {salario}€.")
