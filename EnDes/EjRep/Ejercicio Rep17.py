# Samuel Gutiérrez Merino
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
# Para esto, se registran los días que trabajó y las horas de cada día. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.
num_empleados_gutiérrez = int(input("Introduce la cantidad de empleados que trabajan: "))
total_gutiérrez=0
while  num_empleados_gutiérrez!=0:
    dias_trabajados_gutiérrez=0
    horas_semanales_gutiérrez=0
    sueldo_hora_gutiérrez=0
    i=1
    sueldo_semana_gutiérrez=0
    dias_trabajados_gutiérrez = int(input("Introduce cuantos días de la semana ha trabajado el empleado: "))
    while i<=dias_trabajados_gutiérrez:
        horas_dia_gutiérrez = float(input("Introduce las horas que ha trabajado el empleado ese día: "))
        horas_semanales_gutiérrez+=horas_dia_gutiérrez
        i+=1
    sueldo_hora_gutiérrez = float(input("Introduce el sueldo por hora del empleado: "))
    sueldo_semana_gutiérrez = sueldo_hora_gutiérrez*horas_semanales_gutiérrez
    total_gutiérrez+=sueldo_semana_gutiérrez
    print("Este empleado cobrará", sueldo_semana_gutiérrez, "€ al cabo de una semana")
    num_empleados_gutiérrez-=1
print("En total, la empresa deberá pagar", total_gutiérrez, "€ a sus empleados")