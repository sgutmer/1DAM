# Samuel Gutiérrez Merino
agenda_gutiérrez = {}
while True:
    print("Menú de Agenda:")
    print("")
    print("1. Añadir/Modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    opcion_gutiérrez = input("Ingrese el número de la opción deseada: ")
    if opcion_gutiérrez == "1":
        nombre = input("Ingrese el nombre: ")
        if nombre in agenda_gutiérrez:
            print(f"Teléfono actual: {agenda_gutiérrez[nombre]}")
            modificar = input("¿Desea modificar el teléfono? (s/n): ")
            if modificar.lower() == "s":
                telefono = input("Ingrese el nuevo teléfono: ")
                agenda_gutiérrez[nombre] = telefono
                print("Teléfono modificado correctamente.")
        else:
            telefono = input("Ingrese el teléfono: ")
            agenda_gutiérrez[nombre] = telefono
            print("Contacto añadido correctamente.")
    elif opcion_gutiérrez == "2":
        cadena = input("Ingrese la cadena de búsqueda: ")
        coincidencias = [nombre for nombre in agenda_gutiérrez.keys() if nombre.startswith(cadena)]
        if coincidencias:
            print("Coincidencias encontradas:")
            for nombre in coincidencias:
                print(f"{nombre}: {agenda_gutiérrez[nombre]}")
        else:
            print("No se encontraron coincidencias.")
    elif opcion_gutiérrez == "3":
        nombre = input("Ingrese el nombre a borrar: ")
        if nombre in agenda_gutiérrez:
            confirmar = input(f"¿Está seguro de que desea borrar a {nombre}? (s/n): ")
            if confirmar.lower() == "s":
                del agenda_gutiérrez[nombre]
                print("Contacto borrado correctamente.")
        else:
            print("El contacto no existe en la agenda.")
    elif opcion_gutiérrez == "4":
        if agenda_gutiérrez:
            print("Lista de contactos:")
            for nombre, telefono in agenda_gutiérrez.items():
                print(f"{nombre}: {telefono}")
        else:
            print("La agenda está vacía.")
    elif opcion_gutiérrez == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")