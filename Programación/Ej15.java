package samuelgutmer.ej15;

//Código escrito por Samuel Gutiérrez Merino

import java.util.Scanner;

public class Ej15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresa el primer número: ");
        double a = scanner.nextDouble();

        System.out.println("Ingresa el segundo número: ");
        double b = scanner.nextDouble();

        System.out.println("Ingresa el tercer número: ");
        double c = scanner.nextDouble();

        double mayor = a;

        if (b > mayor) {
            mayor = b;
        }

        if (c > mayor) {
            mayor = c;
        }

        System.out.println("El número mayor es: " + mayor);

        scanner.close();
    }
}