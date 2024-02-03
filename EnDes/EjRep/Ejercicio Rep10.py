# Samuel Gutiérrez Merino
# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
num_tabla = 1
num = 1
while (num_tabla<6):
    print("La tabla del", num_tabla, "es:")
    while (num<11):
        multiplica = num_tabla*num
        print(num_tabla, "x", num, "=", multiplica)
        num = num+1
    num_tabla = num_tabla+1
    num = 1