# Samuel Gutiérrez Merino
# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
# después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
monedas_2_euros = int(input("Cantidad de monedas de 2 euros: "))
monedas_1_euro = int(input("Cantidad de monedas de 1 euro: "))
monedas_50_centimos = int(input("Cantidad de monedas de 50 céntimos: "))
monedas_20_centimos = int(input("Cantidad de monedas de 20 céntimos: "))
monedas_10_centimos = int(input("Cantidad de monedas de 10 céntimos: "))
dinero_euros = (monedas_2_euros * 2) + (monedas_1_euro * 1) + (monedas_50_centimos * 0.5) + (monedas_20_centimos * 0.2) + (monedas_10_centimos * 0.1)
dinero_euros_enteros = int(dinero_euros)
dinero_centimos = int((dinero_euros - dinero_euros_enteros) * 100)
print(f"Tienes {dinero_euros_enteros} euros y {dinero_centimos} céntimos.")