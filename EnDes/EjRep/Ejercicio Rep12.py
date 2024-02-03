# Samuel Gutiérrez Merino
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita 
#  cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.
mes = 1
total = 0
while mes<=12:
    cantidad = float(input("Introduce la cantidad de dinero que has depositado este mes: "))
    mes = mes+1
    total = total+cantidad
    print (f"Llevas ahorrados {total}€")
print(f"Tras depositar dinero por un año, has ahorrado {total}€")