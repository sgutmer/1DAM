// Samuel Gutiérrez Merino
/*
Necesitamos crear un programa para registrar sueldos de hombres y mujeres de una
empresa y detectar si existe brecha salarial entre ambos. El programa pedirá por teclado la
información de N personas distintas (valor también introducido por teclado). Para cada
persona, pedirá su género (0 para varón y 1 para mujer) y su sueldo. Esta información debe
guardarse en una única matriz. Luego se mostrará por pantalla el sueldo medio de cada
género.
*/
package matrices;

import java.util.Scanner;

public class MatricesEj5 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Introduce la cantidad de personas que trabajan en la empresa: ");
        int personas = sc.nextInt();

        // Crear la matriz que almacena la información de cada persona
        double[][] datos = new double[personas][2];
        
        for (int i = 0; i < personas; i++) {
            System.out.println("");
            System.out.println("Persona " + (i + 1));
            System.out.println("Introduce el género de la persona (0 para hombre, 1 para mujer): ");
            int genero = sc.nextInt();
            if (genero!=1 && genero!=0){
                while (genero!=1 && genero!=0){
                    System.out.println("ERROR: El género debe ser 0 o 1, introduce el género de nuevo:");
                    genero = sc.nextInt();
                }
            }
            System.out.println("Introduce su sueldo: ");
            double sueldo = sc.nextDouble();
            if (sueldo<1){
                while (sueldo<1){
                    System.out.println("ERROR: El sueldo no puede ser ni negativo ni 0, introduce el sueldo de nuevo:");
                    sueldo = sc.nextInt();
                }
            }
            // Almacena los datos en la matriz correspondiente
            datos[i][0] = genero;
            datos[i][1] = sueldo;
        }

        // Calcula el sueldo medio de cada género
        double sueldoHombre = 0;
        double sueldoMujer = 0;
        int contadorHombre = 0;
        int contadorMujer = 0;

        for (int i = 0; i < personas; i++) {
            if (datos[i][0] == 0) {
                sueldoHombre += datos[i][1];
                contadorHombre++;
            } else if (datos[i][0] == 1) {
                sueldoMujer += datos[i][1];
                contadorMujer++;
            }
        }

        // Muestra el sueldo medio de ambos géneros
        double sueldoMedioHombre = (contadorHombre > 0) ? sueldoHombre / contadorHombre : 0;
        double sueldoMedioMujer = (contadorMujer > 0) ? sueldoMujer / contadorMujer : 0;
        System.out.println("");
        System.out.println("Sueldo medio de los hombres: " + sueldoMedioHombre+"€");
        System.out.println("Sueldo medio de las mujeres: " + sueldoMedioMujer+"€");

        // Deteta si hay o no brecha salarial, y si la hay, comprueba a quien favorece
        if (sueldoMedioHombre > sueldoMedioMujer) {
            System.out.println("Existe una brecha salarial que favorece a los hombres.");
        } else if (sueldoMedioHombre < sueldoMedioMujer) {
            System.out.println("Existe una brecha salarial que favorece a las mujeres.");
        } else {
            System.out.println("No hay brecha salarial entre hombres y mujeres.");
        }
    }
}
