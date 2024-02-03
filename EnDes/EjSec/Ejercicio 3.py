# Samuel Gutiérrez Merino
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
cateto1 = float(input("Introduce la medida del primer cateto: "));
cateto2 = float(input("Introduce la medida del segundo cateto: "));
hipotenusa = (cateto1**2 + cateto2**2)**0.5;
print(f"La hipotenusa mide {hipotenusa}")