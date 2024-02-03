import java.util.Scanner;

public class Ej36 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce la altura de la X (número impar mayor o igual a 3): ");
        int altura = sc.nextInt();
        // Comprobar si la altura es un número impar mayor o igual a 3
        if (altura % 2 == 1 && altura >= 3) {
            // Pintar la X
            for (int i = 0; i < altura; i++) {
                for (int j = 0; j < altura; j++) {
                    if (i == j || i + j == altura - 1) {
                        System.out.print("*");
                    } else {
                        System.out.print(" ");
                    }
                }
                System.out.println();
            }
        } else {
            // Mostrar mensaje de error si la altura no es válida
            System.out.println("Error: La altura debe ser un número impar mayor o igual a 3.");
        }
        scanner.close();
    }
}
