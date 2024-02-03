# Samuel Gutiérrez Merino
# Dadas dos variables numéricas A y B, que el usuario debe teclear,
# se pide realizar un algoritmo que intercambie los valores de ambas variables
# y muestre cuanto valen al final las dos variables.
A = float(input("Introduce el valor de la variable A: "));
B = float(input("Introduce el valor de la variable B: "));
C = A;
A = B;
B = C;
print(f"Tras invertir los valores, el valor de la variable A es {A}, y el de la variable B es {B}")