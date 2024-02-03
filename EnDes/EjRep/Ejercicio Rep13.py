# Samuel Gutiérrez Merino
# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de estas,
# así como el sueldo que recibirá por las horas trabajadas.
dinero_por_hora_gutiérrez = float(input("Introduce la cantidad que cobras por hora: "))
días_gutiérrez=1
sueldo_gutiérrez=0
horas_totales_gutiérrez=0
while días_gutiérrez!=7:
    días_gutiérrez+=1
    horas_gutiérrez = float(input("Introduce la cantidad de horas que has trabajado hoy: "))
    sueldo_día_gutiérrez = dinero_por_hora_gutiérrez*horas_gutiérrez
    horas_totales_gutiérrez = horas_totales_gutiérrez+horas_gutiérrez
    sueldo_gutiérrez = sueldo_gutiérrez+sueldo_día_gutiérrez
print("Has trabajado", horas_totales_gutiérrez, "horas esta semana")
print("Has cobrado", sueldo_gutiérrez,"€ esta semana")