# Samuel Gutiérrez Merino
# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. 
# Calcula y muestra la distancia entre ellos.
x1 = float(input("Introduce la coordenada x del primer punto: "));
y1 = float(input("Introduce la coordenada y del primer punto: "));
x2 = float(input("Introduce la coordenada x del segundo punto: "));
y2 = float(input("Introduce la coordenada y del segundo punto: "));
dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5;
print(f"La distancia entre los 2 puntos es de {dist} unidades")