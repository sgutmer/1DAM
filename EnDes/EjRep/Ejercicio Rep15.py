# Samuel Gutiérrez Merino
#  Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
# He de aclara que para este ejercicio he encontrado 2 posibilidades:
# 1: Cada mes la cantidad a pagar se incrementa sumando a la cantidad anterior +0€ adicionales (10€/mes, 20€/mes, 30€/mes, 40€/mes, etc.)
# 2: Cada mes la cantidad a pagar se duplica (10€/mes, 20€/mes, 40€/mes, 80€/mes, etc.)
# Debido a la naturaleza de esta actividad, resolveré ambas posibilidades, a pesar que la sgunda es mmuy poco realista, pero nunca viene mal dejarlo todo claro
mes_gutiérrez = 1
total_gutiérrez = 0
pago_mes_gutiérrez = 10
print("Posibilidad 1:")
print("")
print("Deberás pagar 10 € el primer mes")
while mes_gutiérrez!=21:
    total_gutiérrez = total_gutiérrez + pago_mes_gutiérrez
    pago_mes_gutiérrez+=10
    print("Deberás pagar", pago_mes_gutiérrez,"€ el mes", mes_gutiérrez)
    mes_gutiérrez+=1
print("La cantidad total que será pagada al cabo de 20 meses será de", total_gutiérrez,"€")
print("")
print("-----------------------------------------")
print("")
print("Posibilidad 2:")
print("")
mes_gutiérrez = 1
total_gutiérrez = 0
pago_mes_gutiérrez = 10
print("Deberás pagar 10 € el primer mes")
while mes_gutiérrez!=21:
    total_gutiérrez = total_gutiérrez + pago_mes_gutiérrez
    pago_mes_gutiérrez*=2
    print("Deberás pagar", pago_mes_gutiérrez,"€ el mes", mes_gutiérrez)
    mes_gutiérrez+=1
print("La cantidad total que será pagada al cabo de 20 meses será de", total_gutiérrez,"€")