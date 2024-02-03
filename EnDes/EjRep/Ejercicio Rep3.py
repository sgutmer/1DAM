# Samuel Gutiérrez Merino
# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
num = int(input("Introduce un número: "))
total = num
contador = 0
while (num!=0):
    num = int(input("Introduce un número: "))
    contador = contador+1
    total = total + num
media = total/contador
print("La suma total de todos los números es",total)
print("Y la media de estos es",media)