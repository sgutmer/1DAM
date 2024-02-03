# Samuel Gutiérrez Merino
# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
nom = input("Introduce tu nombre: ")
cont = input("Introduce tu contraseña: ")
if (nom=="pepe" and cont=="asdasd"):
    print("Acceso concedido, bienvenido Pepe")
else:
    print("Acceso denegado, el nombre o la contraseña son erróneos")