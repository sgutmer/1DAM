# Samuel Gutiérrez Merino
# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. 
# Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.
lista_meses_gutiérrez = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mes_gutiérrez = int(input("Introduce un mes del año y yo te diré cuantos días tiene: "))
if mes_gutiérrez<1 or mes_gutiérrez>12:
    while mes_gutiérrez<1 or mes_gutiérrez>12:
        mes_gutiérrez = int(input("Hay 12 meses, introduce un número entre el 1 y el 12: "))
mes_gutiérrez-=1
print("Ese mes tiene", lista_meses_gutiérrez[mes_gutiérrez], "días")