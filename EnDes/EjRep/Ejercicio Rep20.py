# Samuel Gutiérrez Merino
# Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
# Pedir al usuario cuántos números primos quiere mostrar
cantidad_gutiérrez = int(input("Cuántos números primos quieres mostrar: "))
contador = 0
num_gutiérrez = 2
while contador < cantidad_gutiérrez:
    primo_gutiérrez = True
    for i in range(2, num_gutiérrez):
        if num_gutiérrez % i == 0:
            primo_gutiérrez = False
            break
    if primo_gutiérrez==True:
        print(num_gutiérrez, end=' ')
        contador += 1
    num_gutiérrez += 1