# Samuel Gutiérrez Merino
# Escribir una programa que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre primer apellido-n.txt la tabla de multiplicar de ese número, done n es el número introducido.
def tabla_num_gutierrez(numero_gutierrez):
    if 1 <= numero_gutierrez <= 10:
        nombre_archivo_gutierrez = f'gutierrez-{numero_gutierrez}.txt'
        with open(nombre_archivo_gutierrez, 'w') as archivo:
            for i in range(1, 11):
                resultado_gutierrez = numero_gutierrez * i
                linea_gutierrez = f'{numero_gutierrez} x {i} = {resultado_gutierrez}\n'
                archivo.write(linea_gutierrez)
        print(f'Tabla de multiplicar del {numero_gutierrez} guardada en {nombre_archivo_gutierrez}')
    else:
        print('Error: Debes introducir un número entre 1 y 10.')
try:
    numero_gutierrez = int(input('Introduce un número entero entre 1 y 10: '))
    tabla_num_gutierrez(numero_gutierrez)
except ValueError:
    print('Error: Debes introducir un número entero válido.')