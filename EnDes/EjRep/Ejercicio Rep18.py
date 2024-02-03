# Samuel Gutiérrez Merino
# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
import time
horas_gutiérrez=0
minutos_gutierrez=0
segundos_gutiérrez=0
while True:
    segundos_gutiérrez+=1
    if segundos_gutiérrez==60:
        segundos_gutiérrez=0
        minutos_gutierrez+=1
    else:
        if minutos_gutierrez==60:
            minutos_gutierrez=0
            horas_gutiérrez+=1
    print(horas_gutiérrez,":",minutos_gutierrez,":",segundos_gutiérrez)
    time.sleep(1)