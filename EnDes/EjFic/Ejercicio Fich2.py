# Samuel Gutiérrez Merino
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero primerapellido-n.txt con la tabla de multiplicar de ese número, 
# donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
num_gutierrez = int(input('Introduce un número entre 1 y 10: '))
fichero_gutierrez = 'gutierrez-' + str(num_gutierrez) + '.txt'
try: 
    f = open(fichero_gutierrez, 'r')
except FileNotFoundError:
    print("No existe el archivo para la tabla del", num_gutierrez)
else:
    print(f.read())
    f.close()