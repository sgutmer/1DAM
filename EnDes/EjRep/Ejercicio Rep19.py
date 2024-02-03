# Samuel Gutiérrez Merino
#
print("Bienvenido, que menú desea ver:")
print("1: Menú 1")
print("2: Menú 2")
print("3: Menú 3")
print("4: Menú 4")
print("X: Salir")

while True:
    opción_gutiérrez = input("Ingrese el número de la opción que desea: ")
    if opción_gutiérrez == "1":
        print("Ha elegido el menú 1")
        print("Filete de ternera con salteado vegetal y una bebida a elegir")
    elif opción_gutiérrez == "2":
        print("Ha elegido el menú 2:")
        print("Sandwich completo con patatas de gajo fritas y una bebida a elegir")
    elif opción_gutiérrez == "3":
        print("Ha elegido el menú 3")
        print("Pescado a la lancha con patatas asadas y bebida a elegir")
    elif opción_gutiérrez == "4":
        print("Ha elegido el menú 4")
        print("Pasta carbonara y bebida a elegir")
    elif opción_gutiérrez == "X":
        print("Esperamos que disfrute de su pedido")
        break
    else:
        print("Opción no válida, elige una opción válida.")