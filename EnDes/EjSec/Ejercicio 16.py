# Samuel Gutiérrez Merino
# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. 
# El que está detrás viaja a una velocidad mayor.
# Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) 
# y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) 
# alcanzará el vehículo más rápido al otro.
d = float(input("Indica la distancia (en km) que hay entre los coches: "))
v1 = float(input("¿A qué velocidad (km/h) va el vehículo lento?: "))
v2 = float(input("¿A qué velocidad (km/h) va el vehículo rápido?: "))
T_h = d / (v2 - v1)
T_min = T_h * 60
print(f"El vehículo más rápido alcanzará al otro en {T_min} minutos.")