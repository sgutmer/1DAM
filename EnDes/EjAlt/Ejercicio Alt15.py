# Samuel Gutiérrez Merino
# El director de una escuela está organizando un viaje de estudios, 
# y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes 
# por el servicio. La forma de cobrar es la siguiente: 
# si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
# de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, 
# el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses y
# lo que debe pagar cada alumno por el viaje.

alumnos = int(input("Introduce le número de alumnos que irán al viaje: "))
if alumnos>=100:
    costoalumno = 65
elif alumnos>=50 and alumnos<=99:
    costoalumno = 70
elif alumnos>=30 and alumnos<=49:
    costoalumno = 95
else:
    costoalumno = 4000/alumnos
if alumnos>30:
    total = costoalumno * alumnos
else:
    total = 4000

print(f"Entre todos los alumnos deberán pagar {total}€")
print(f"Y cada alumno deberá pagar {costoalumno}€")
