# Samuel Gutiérrez Merino
# Escribir un programa que pida dos números n y m entre 1 y 10, lea el fichero primerapellido-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
def mostrar_linea_tabla_multiplicar(n, m):
    if 1 <= n_gutierrez <= 10 and 1 <= m_gutierrez <= 10:
        nombre_archivo_gutierrez = f'gutierrez-{n}.txt'
        try:
            with open(nombre_archivo_gutierrez, 'r') as archivo:
                lineas_gutierrez = archivo.readlines()
                if 1 <= m <= len(lineas_gutierrez):
                    print(f'Línea {m} de la tabla de multiplicar del {n}: {lineas_gutierrez[m - 1]}')
                else:
                    print(f'Error: El número {m} está fuera del rango en el archivo {nombre_archivo_gutierrez}.')
        except FileNotFoundError:
            print(f'Error: El archivo {nombre_archivo_gutierrez} no existe.')
    else:
        print('Error: Debes introducir dos números enteros entre 1 y 10.')
try:
    n_gutierrez = int(input('Introduce un número entre 1 y 10: '))
    m_gutierrez = int(input('Introduce otro número entre 1 y 10: '))
    mostrar_linea_tabla_multiplicar(n_gutierrez, m_gutierrez)
except ValueError:
    print('Error: Debes introducir dos números válidos.')