# Samuel Gutiérrez Merino
# Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia.
# El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:
# Zona	Ubicación	Costo/gramo
# 1	América del Norte	24.00 euros
# 2	América Central	20.00 euros
# 3	América del Sur	21.00 euros
# 4	Europa	10.00 euros
# 5	Asia	18.00 euros
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
peso = int(input("Introduce el peso del paquete en gramos: "))
if peso<=5000:
    print("[1] America del Norte = 24€/g")
    print("[1] América Central  = 20€/g")
    print("[3] América del Sur = 21€/g")
    print("[4] Europa = 10€/g")
    print("[5] Asia = 18€/g")
    destino = int(input("Introduce el continente al que se entregará el paquete siguiendo la guía: "))
    if destino==1:
        coste=peso*24
        print("El coste será de", coste,"€")
    elif destino==2:
        coste=peso*20
        print("El coste será de", coste,"€")
    elif destino==3:
        coste=peso*21
        print("El coste será de", coste,"€")
    elif destino==4:
        coste=peso*10
        print("El coste será de", coste,"€")
    elif destino==5:
        coste=peso*18
        print("El coste será de", coste,"€")
    else:
        print("ERROR: El destino del paquete debe seguir la guía anteriormente proporcionada")
else:
    print("Lo sentimos, por normas de la compañía no aceptamos paquetes con un peso superior a 5000g (5kg)")