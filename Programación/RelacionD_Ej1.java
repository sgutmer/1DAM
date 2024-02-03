// Samuel Gutiérrez Merino
/*
ENUNCIADO:
Se desean guardar y representar las notas de 5 alumnos en 4 asignaturas (n�meros aleatorios con decimales entre 0 y 10) en una matriz.
Adem�s, tanto para cada asignatura como para cada alumno, se precisa obtener y almacenar la nota m�xima, m�nima y la media aritm�tica

EXPLICACI�N:
He creado una matriz que almacena las distintas notas de los alumns en cada asignatura
Luego, tengo 6 vectores que almacenan las notas m�nima, m�xima y media de cada alumno o asignatura
Por �ltimo, imprimo los resultados como 2 peque�as listas (ALUMNOS y ASIGNATURAS), donde se muestran estos datos
(Lo siento, no consegu�a� que funcionase de otra manera as� que me decant� por esta opci�n)
*/
package reld.ej1;

import java.util.Random;

public class RelacionD_Ej1 {
    public static void main(String[] args) {
        // Definir el n�mero de alumnos y asignaturas
        final int ALUMNOS = 5;
        final int ASIGNATURAS = 4;

        // Crear la matriz para almacenar las notas
        double[][] notas = new double[ALUMNOS][ASIGNATURAS];

        // Llenar la matriz con n�meros aleatorios entre 0 y 10
        Random random = new Random();
        for (int i = 0; i < ALUMNOS; i++) {
            for (int j = 0; j < ASIGNATURAS; j++) {
                notas[i][j] = random.nextDouble() * 10;
            }
        }

        // Crear matrices para almacenar notas m�nimas, m�ximas y medias
        double[] notaMinimaAsignatura = new double[ASIGNATURAS];
        double[] notaMaximaAsignatura = new double[ASIGNATURAS];
        double[] mediaAsignatura = new double[ASIGNATURAS];

        double[] notaMinimaAlumno = new double[ALUMNOS];
        double[] notaMaximaAlumno = new double[ALUMNOS];
        double[] mediaAlumno = new double[ALUMNOS];

        // Calcular y almacenar estad�sticas por asignatura
        for (int j = 0; j < ASIGNATURAS; j++) {
            double notaMaxima = Double.MIN_VALUE;
            double notaMinima = Double.MAX_VALUE;
            double sumaNotas = 0;

            for (int i = 0; i < ALUMNOS; i++) {
                double nota = notas[i][j];

                // Actualizar nota m�xima y m�nima
                notaMaxima = Math.max(notaMaxima, nota);
                notaMinima = Math.min(notaMinima, nota);

                // Acumular notas para calcular la media
                sumaNotas += nota;
            }

            // Calcular media
            double media = sumaNotas / ALUMNOS;

            // Almacenar estad�sticas en matrices correspondientes
            notaMaximaAsignatura[j] = notaMaxima;
            notaMinimaAsignatura[j] = notaMinima;
            mediaAsignatura[j] = media;
        }

        // Calcular y almacenar estad�sticas por alumno
        for (int i = 0; i < ALUMNOS; i++) {
            double notaMaxima = Double.MIN_VALUE;
            double notaMinima = Double.MAX_VALUE;
            double sumaNotas = 0;

            for (int j = 0; j < ASIGNATURAS; j++) {
                double nota = notas[i][j];

                // Actualizar nota m�xima y m�nima
                notaMaxima = Math.max(notaMaxima, nota);
                notaMinima = Math.min(notaMinima, nota);

                // Acumular notas para calcular la media
                sumaNotas += nota;
            }

            // Calcular media
            double media = sumaNotas / ASIGNATURAS;

            // Almacenar estad�sticas en matrices correspondientes
            notaMaximaAlumno[i] = notaMaxima;
            notaMinimaAlumno[i] = notaMinima;
            mediaAlumno[i] = media;
        }

        // Mostrar las estad�sticas almacenadas
        System.out.println("ASIGNATURAS:");
        System.out.println("");
        for (int j = 0; j < ASIGNATURAS; j++) {
            System.out.println("Asignatura " + (j + 1) + ":");
            System.out.println("  Nota m�xima: " + notaMaximaAsignatura[j]);
            System.out.println("  Nota m�nima: " + notaMinimaAsignatura[j]);
            System.out.println("  Media: " + mediaAsignatura[j]);
            System.out.println();
        }

        System.out.println("ALUMNOS:");
        System.out.println("");
        for (int i = 0; i < ALUMNOS; i++) {
            System.out.println("Alumno " + (i + 1) + ":");
            System.out.println("  Nota m�xima: " + notaMaximaAlumno[i]);
            System.out.println("  Nota m�nima: " + notaMinimaAlumno[i]);
            System.out.println("  Media: " + mediaAlumno[i]);
            System.out.println();
        }
    }
}
