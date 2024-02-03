package samuelgutmer.ej10;
// Código escrito por Samuel Gutiérrez Merino
import java.util.Scanner;

public class Ej10{
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            
            System.out.print("Ingrese el primer número: ");
            double a = sc.nextDouble();
            
            System.out.print("Ingrese el segundo número: ");
            double b = sc.nextDouble();
            
            double suma = a + b;
            double resta = a - b;
            double producto = a * b;
            double division = 0.0;
            
            if (b != 0) {
                division = a / b;
            } else {
                System.out.println("No se puede dividir por cero.");
            }
            
            System.out.println("Suma: " + suma);
            System.out.println("Resta: " + resta);
            System.out.println("Producto: " + producto);
            
            if (b != 0) {
                System.out.println("División: " + division);
            }
        }
    }
}