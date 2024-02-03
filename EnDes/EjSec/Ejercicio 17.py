# Samuel Gutiérrez Merino
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.
h = int(input("Ingresa las horas del momento de la salida: "))
min = int(input("Ingresa los minutos del momento de la salida: "))
s = int(input("Ingresa los segundos del momento de la salida: "))
T = int(input("Ingresa el tiempo de viaje en segundos: "))
T_seg = h * 3600 + min * 60 + s
T_t_seg = T_seg + T
h_llegada = T_t_seg // 3600
min_llegada = (T_t_seg % 3600) // 60
s_llegada = T_t_seg % 60
print(f"Hora de llegada a la ciudad B será a las {h_llegada}:{min_llegada}:{s_llegada}")