# Samuel Gutiérrez Merino
# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
num = int(input("Introduce un número y te daré la tabla de multiplicar de este: "))
contador = 1
while (contador<=10):
    multiplica = num*contador
    print(num, "x", contador, "=", multiplica)  
    contador = contador+1