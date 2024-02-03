# Samuel Gutiérrez Merino
# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.
lado1 = float(input("Introduce la medida del primer lado: "))
lado2 = float(input("Introduce la medida del segundo lado: "))
lado3 = float(input("Introduce la medida del tercer lado: "))
if lado1**2==(lado2**2+lado3**2) or lado2**2==(lado1**2+lado3**2) or lado3**2==(lado2**2+lado1**2):
    print("El triángulo es rectángulo")
else:
    if (lado1==lado2==lado3):
        print("El triángulo es equilátero")
    elif (lado1==lado2!=lado3) or (lado1!=lado2==lado3) or (lado1==lado3!=lado2):
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")