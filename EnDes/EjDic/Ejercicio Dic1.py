# Samuel Gutierrez Merino
# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 
# hasta el número indicado, y los valores sean los cuadrados de las claves.
num_gutiérrez = int(input("Escrine un número: "))
diccionario_gutiérrez = {}
for clave_gutiérrez in range(1, num_gutiérrez + 1):
    diccionario_gutiérrez[clave_gutiérrez] = clave_gutiérrez ** 2
print("El diccionario es que va desde el 1 hasta el",num_gutiérrez,"es:")
print(diccionario_gutiérrez)