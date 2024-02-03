# Samuel Gutiérrez Merino
#  De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
# Nombre: Lista para guardar los nombres de los conductores.
# kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.
conductores_gutiérrez = ["Juan", "María", "Carlos"]
kms_gutiérrez = [
    [50, 75, 40, 100, 90],  
    [30, 40, 25, 80, 60],   
    [70, 60, 45, 120, 110] 
]
total_kms_gutiérrez = []
for i in range(len(conductores_gutiérrez)):
    total_gutiérrez = sum(kms_gutiérrez[i])
    total_kms_gutiérrez.append(total_gutiérrez)
print("Resumen de Kilómetros:")
for i in range(len(conductores_gutiérrez)):
    print(f"{conductores_gutiérrez[i]}: {total_kms_gutiérrez[i]} kilómetros")
print("\nDetalles por Conductor:")
for i in range(len(conductores_gutiérrez)):
    print(f"{conductores_gutiérrez[i]}: {kms_gutiérrez[i]} kilómetros")