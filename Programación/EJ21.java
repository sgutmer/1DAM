//  Samuel Gutiérrez Merino
package ej21;

import java.util.Scanner;

public class EJ21 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int opcion = menu();
            double radio;
            switch (opcion) {
                case 1:
                    radio = pideRadio();
                    System.out.println("La circunferencia mide: " + circunferencia(radio)+" u (unidades)");
                    break;
                case 2:
                    radio = pideRadio();
                    System.out.println("El área de la circunferencia es de: " + area(radio)+ "u2 (unidades cuadradas)");
                    break;
                case 3:
                    radio = pideRadio();
                    System.out.println("El volumen de la circunferencia es de: " + volumen(radio)+" u3 (unidades cúbicas)");
                    break;
                case 4:
                    radio = pideRadio();
                    System.out.println("Circunferencia: " + circunferencia(radio));
                    System.out.println("Área: " + area(radio));
                    System.out.println("Volumen: " + volumen(radio));
                    break;
                case 5:
                    System.out.println("Has cerrado el programa, adiós");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Opción no válida. Inténtalo de nuevo.");
            }
        }
    }

    // Muestra el menú y devuelve la opción elegida
    private static int menu() {
        Scanner sc = new Scanner(System.in);

        System.out.println("\nMenú:");
        System.out.println("1. Calcular circunferencia");
        System.out.println("2. Calcular área");
        System.out.println("3. Calcular volumen");
        System.out.println("4. Calcular todas a la vez");
        System.out.println("5. Salir del programa");

        System.out.print("Elige una opción: ");
        return sc.nextInt();
    }

    // Pide al usuario que introduzca el radio y lo devuelve
    private static double pideRadio() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce el radio: ");
        return sc.nextDouble();
    }

    // Calcula la circunferencia y la devuelve
    private static double circunferencia(double r) {
        return 2 * Math.PI * r;
    }

    // Calcula el área y la devuelve
    private static double area(double r) {
        return Math.PI * Math.pow(r, 2);
    }

    // Calcula el volumen y lo devuelve
    private static double volumen(double r) {
        return (4.0 / 3.0) * Math.PI * Math.pow(r, 3);
    }
}