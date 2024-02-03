# Samuel Gutiérrez Merino
# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), 
# realiza un programa que cuente cuantas palabras tiene.
cadenas_gutiérrez = input("Escribe algo, tan largo como quieras: ")
espacios_gutiérrez = 0
espacios_gutiérrez = cadenas_gutiérrez.count(" ")
espacios_gutiérrez+=1
print("Hay", espacios_gutiérrez, "palabras en el texto que has escrito")