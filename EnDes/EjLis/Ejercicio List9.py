# Samuel Gutiérrez Merino
# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
# La temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
lista_temp_min_gutiérrez =  [12.3, 14.6, 13, 16.8, 13.7]
lista_temp_max_gutiérrez =  [21.4, 26.3, 23.5, 22.4, 20.8]
lista_temp_media_gutiérrez = []
i = 0
j = 0
while i != 5:
    media = (lista_temp_min_gutiérrez[i]+lista_temp_max_gutiérrez[i])/2
    lista_temp_media_gutiérrez.append(media)
    i+=1
print("La temperatura media de cada día es:")
for temp in lista_temp_media_gutiérrez:
    print(temp)
while i<5:
    if lista_temp_min_gutiérrez[i]>temp_min:
        temp_min = lista_temp_min_gutiérrez[i]
        j = lista_temp_min_gutiérrez.index(temp_min)
    i+=1
print("Y el día con la menor temperatura es: el día Nº", lista_temp_min_gutiérrez[j])
temp_gutiérrez = float(input("Introduce una temperatura: "))
i = 0
while i<5:
    if temp_gutiérrez == lista_temp_max_gutiérrez[i]:
        temp_valida_gutiérrez = True
        break
    else:
        temp_valida_gutiérrez = False
    i+=1
if temp_valida_gutiérrez == True:
    print ("La temperatura coincide con la temperatura del día Nº", lista_temp_max_gutiérrez.index(temp_gutiérrez))
elif temp_valida_gutiérrez == False:
    print("La temperatura introducida no coincide con ninguna de las temperaturas")