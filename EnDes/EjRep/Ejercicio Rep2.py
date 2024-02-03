# Samuel Gutiérrez Merino
#  Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
#  A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan
# (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado),
# si se llega al limite de intentos te muestra el número que había generado.
import random
num_adivinar_gutierrez = random.randint(1,100)
intentos = 1
print ("Intenta adivinar un número del 1 al 100")
num_gutierrez = int(input("Ingresa aquí un número para intentar adivinar: "))
while num_gutierrez != num_adivinar_gutierrez:
    if num_gutierrez<1 or num_gutierrez>100:
        print("JA, has perdido un intento, ahora te aguantas y juegas con un intento menos")
    elif num_gutierrez>num_adivinar_gutierrez:
        print("El número es menor que", num_gutierrez)
    elif num_gutierrez<num_adivinar_gutierrez:
        print("El número es mayor que", num_gutierrez)
    num_gutierrez = int(input("Inténtalo de nuevo: "))
    if intentos==9:
        break
    intentos+=1
if num_gutierrez==num_adivinar_gutierrez:
    print("¡Acertaste!, solo te tomó", intentos, "intentos")
else:
    print("Uf, parece que no se te da bien esto de adivinar números")