# Samuel Gutiérrez Merino
# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# He informa si hemos introducido algún número igual a los límites del intervalo.
lim_inf = float(input("Introduce el valor del límite inferior: "))
lim_sup = float(input("Introduce el valor del límite superior: "))
igual = False
num = 1
dentro = 0
fuera = 0
if (lim_inf>lim_sup):
    while(lim_inf>lim_sup):
        lim_sup = int(input("INCORRECTO, el límite superior debe ser mayor que el inferior. Vuelve a introducir el valor del límite superior: "))
while (num!=0):
    num = float(input("Introduce un número: "))
    if (num>lim_sup or num<lim_inf):
        fuera = fuera+1
    elif (num<lim_sup and num>lim_inf):
        dentro = dentro+1
    elif (num==lim_sup or num==lim_inf):
        igual = True
fuera = fuera-1
if (igual==True):
    print(f"Has introducido {dentro} números dentro del intervalo, {fuera} números fuera del intervalo y se ha introducido al menos 1 número igual a alguno de los límites")
else:
    print(f"Has introducido {dentro} números dentro del intervalo, {fuera} números fuera del intervalo, pero no se ha introducido ningún número igual a alguno de los límites")