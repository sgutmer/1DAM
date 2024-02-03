# Samuel Gutiérrez Merino
# Vamos a crear un programa que tenga el siguiente menú:
# 1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# 2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# 3. Longitud de la lista: te muestra el número de elementos de la lista.
# 4. Eliminar el último número: Muestra el último número de la lista y lo borra.
# 5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
# 6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# 7. Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# 8. Mostrar números: Muestra los números de la lista
# 9. Salir
lista_gutiérrez = []

def agregar_numero():
    numero_gutiérrez = int(input("Ingrese un número para agregar a la lista: "))
    lista_gutiérrez.append(numero_gutiérrez)
    print(f"¡Número {numero_gutiérrez} agregado a la lista!")

def agregar_en_posicion():
    numero_gutiérrez = int(input("Ingrese un número para agregar a la lista: "))
    posicion_gutiérrez = int(input("Ingrese la posición en la que desea agregar el número (a partir de 1): "))
    if 1 <= posicion_gutiérrez <= len(lista_gutiérrez) + 1:
        lista_gutiérrez.insert(posicion_gutiérrez - 1, numero_gutiérrez)
        print(f"¡Número {numero_gutiérrez} agregado en la posición {posicion_gutiérrez}!")

    else:
        print("La posición ingresada no es válida.")

def longitud_lista():
    print(f"La longitud de la lista es: {len(lista_gutiérrez)}")

def eliminar_ultimo_numero():
    if lista_gutiérrez:
        ultimo_numero_gutiérrez = lista_gutiérrez.pop()
        print(f"Se eliminó el último número de la lista: {ultimo_numero_gutiérrez}")
    else:
        print("La lista está vacía.")

def eliminar_numero():
    if lista_gutiérrez:
        posicion_gutiérrez = int(input("Ingrese la posición del número que desea eliminar (a partir de 1): "))
        if 1 <= posicion_gutiérrez <= len(lista_gutiérrez):
            numero_eliminado_gutiérrez = lista_gutiérrez.pop(posicion_gutiérrez - 1)
            print(f"Se eliminó el número {numero_eliminado_gutiérrez} de la lista.")
        else:
            print("La posición ingresada no es válida.")
    else:
        print("La lista está vacía.")

def contar_numeros():
    if lista_gutiérrez:
        numero_gutiérrez = int(input("Ingrese un número para contar en la lista: "))
        cantidad = lista_gutiérrez.count(numero_gutiérrez)
        print(f"El número {numero_gutiérrez} aparece {cantidad} veces en la lista.")
    else:
        print("La lista está vacía.")

def posiciones_numero():
    if lista_gutiérrez:
        numero_gutiérrez = int(input("Ingrese un número para encontrar sus posiciones en la lista: "))
        posiciones_gutiérrez = [i + 1 for i, x in enumerate(lista_gutiérrez) if x == numero_gutiérrez]
        if posiciones_gutiérrez:
            print(f"El número {numero_gutiérrez} está en las posiciones: {', '.join(map(str, posiciones_gutiérrez))}")
        else:
            print(f"El número {numero_gutiérrez} no está en la lista.")
    else:
        print("La lista está vacía.")

def mostrar_numeros():
    if lista_gutiérrez:
        print("Números en la lista:", lista_gutiérrez)
    else:
        print("La lista está vacía.")

while True:
    print("Menú:")
    print("1. Añadir número a la lista")
    print("2. Añadir número en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == '1':
        agregar_numero()
    elif opcion == '2':
        agregar_en_posicion()
    elif opcion == '3':
        longitud_lista()
    elif opcion == '4':
        eliminar_ultimo_numero()
    elif opcion == '5':
        eliminar_numero()
    elif opcion == '6':
        contar_numeros()
    elif opcion == '7':
        posiciones_numero()
    elif opcion == '8':
        mostrar_numeros()
    elif opcion == '9':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 9.")
