# Samuel Gutiérrez Merino
# Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
i=1
j=0
lista_normal_gutiérrez=[]
lista_inversa_gutiérrez=[]
while i!=6:
    cadena_gutiérrez = input("Introduce una cadena: ")
    lista_normal_gutiérrez.append(cadena_gutiérrez)
    i+=1
lista_inversa_gutiérrez = lista_normal_gutiérrez.copy()
lista_inversa_gutiérrez.reverse()
i=0
print("Ahora, se mostrarán por pantalla las cadenas introducidas en orden inverso:")
while i!=5:
    print(lista_inversa_gutiérrez[i])
    i+=1