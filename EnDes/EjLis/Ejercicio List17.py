# Samuel Gutiérrez Merino
#  Crear un programa que añada números a una lista hasta que introducimos un número negativo. 
# A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. 
# Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.
lista_original_gutiérrez = []
while True:
    numero = int(input("Ingrese un número (introduzca un número negativo para finalizar): "))
    if numero < 0:
        break
    lista_original_gutiérrez.append(numero)
lista_sin_duplicados = list(set(lista_original_gutiérrez))
print("Lista original:")
print(lista_original_gutiérrez)
print("Lista sin duplicados:")
print(lista_sin_duplicados)