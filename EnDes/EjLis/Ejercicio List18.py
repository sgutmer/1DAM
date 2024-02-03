# Samuel Gutiérrez Merino
# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
# Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# Eliminar: Me pide una cadena, y la elimina de la lista.
# Mostrar: Muestra la lista de cadenas
# Terminar
lista_palabras_gutiérrez = []
j=1
i = int(input("¿Cuántas cadenas desea introducir? "))
while j<=i:
    palabra_gutiérrez = input("")
    lista_palabras_gutiérrez.append(palabra_gutiérrez)
    j+=1

while True:
    print("Menú:")
    print("1. Contar palabra en la lista")
    print("2. Modificar palabra en la lista")
    print("3. Eliminar palabra de la lista")
    print("4. Mostrar lista de palabras")
    print("5. Terminar")
    opcion_gutiérrez = input("Ingrese el número de la opción que desea realizar: ")
    if opcion_gutiérrez == '1':
        palabra_a_contar = input("Ingrese la palabra que desea contar: ")
        cantidad = lista_palabras_gutiérrez.count(palabra_a_contar)
        print(f"La palabra '{palabra_a_contar}' aparece {cantidad} veces en la lista.")
    elif opcion_gutiérrez == '2':
        palabra_a_modificar = input("Ingrese la palabra que desea modificar: ")
        nueva_palabra = input("Ingrese la nueva palabra: ")
        lista_palabras_gutiérrez = [nueva_palabra if palabra == palabra_a_modificar else palabra for palabra in lista_palabras_gutiérrez]
        print(f"Palabra '{palabra_a_modificar}' modificada por '{nueva_palabra}' en la lista.")
    elif opcion_gutiérrez == '3':
        palabra_a_eliminar = input("Ingrese la palabra que desea eliminar: ")
        lista_palabras_gutiérrez = [palabra for palabra in lista_palabras_gutiérrez if palabra != palabra_a_eliminar]
        print(f"Palabra '{palabra_a_eliminar}' eliminada de la lista.")
    elif opcion_gutiérrez == '4':
        print("Lista de palabras:", lista_palabras_gutiérrez)
    elif opcion_gutiérrez == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")