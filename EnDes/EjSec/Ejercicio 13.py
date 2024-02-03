# Samuel Gutiérrez Merino
# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
# Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?
num = float(input("Introduce un número: "));
raizcuad = num**0.5;
raizcub = num**(1/3);
print(f"La raíz cuadrada de {num} es {raizcuad}, y la raíz cúbica es {raizcub}")