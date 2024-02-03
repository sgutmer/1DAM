// Samuel GutiÃ©rrez Merino
/*
ENUNCIADO:
Se desean guardar y representar las notas de 5 alumnos en 4 asignaturas (números aleatorios con decimales entre 0 y 10) en una matriz.
Además, tanto para cada asignatura como para cada alumno, se precisa obtener y almacenar la nota máxima, mínima y la media aritmética

EXPLICACIÓN:
He creado una matriz que almacena las distintas notas de los alumns en cada asignatura
Luego, tengo 6 vectores que almacenan las notas mí­nima, máxima y media de cada alumno o asignatura
Por último, imprimo los resultados como 2 pequeñas listas (ALUMNOS y ASIGNATURAS), donde se muestran estos datos
(Lo siento, no conseguía­ que funcionase de otra manera así­ que me decanté por esta opción)
*/
package reld.ej1;

import java.util.Random;

public class RelacionD_Ej1 {
    public static void main(String[] args) {
        // Definir el número de alumnos y asignaturas
        final int ALUMNOS = 5;
        final int ASIGNATURAS = 4;

        // Crear la matriz para almacenar las notas
        double[][] notas = new double[ALUMNOS][ASIGNATURAS];

        // Llenar la matriz con números aleatorios entre 0 y 10
        Random random = new Random();
        for (int i = 0; i < ALUMNOS; i++) {
            for (int j = 0; j < ASIGNATURAS; j++) {
                notas[i][j] = random.nextDouble() * 10;
            }
        }

        // Crear matrices para almacenar notas mí­nimas, máximas y medias
        double[] notaMinimaAsignatura = new double[ASIGNATURAS];
        double[] notaMaximaAsignatura = new double[ASIGNATURAS];
        double[] mediaAsignatura = new double[ASIGNATURAS];

        double[] notaMinimaAlumno = new double[ALUMNOS];
        double[] notaMaximaAlumno = new double[ALUMNOS];
        double[] mediaAlumno = new double[ALUMNOS];

        // Calcular y almacenar estadí­sticas por asignatura
        for (int j = 0; j < ASIGNATURAS; j++) {
            double notaMaxima = Double.MIN_VALUE;
            double notaMinima = Double.MAX_VALUE;
            double sumaNotas = 0;

            for (int i = 0; i < ALUMNOS; i++) {
                double nota = notas[i][j];

                // Actualizar nota máxima y mí­nima
                notaMaxima = Math.max(notaMaxima, nota);
                notaMinima = Math.min(notaMinima, nota);

                // Acumular notas para calcular la media
                sumaNotas += nota;
            }

            // Calcular media
            double media = sumaNotas / ALUMNOS;

            // Almacenar estadí­sticas en matrices correspondientes
            notaMaximaAsignatura[j] = notaMaxima;
            notaMinimaAsignatura[j] = notaMinima;
            mediaAsignatura[j] = media;
        }

        // Calcular y almacenar estadí­sticas por alumno
        for (int i = 0; i < ALUMNOS; i++) {
            double notaMaxima = Double.MIN_VALUE;
            double notaMinima = Double.MAX_VALUE;
            double sumaNotas = 0;

            for (int j = 0; j < ASIGNATURAS; j++) {
                double nota = notas[i][j];

                // Actualizar nota máxima y mí­nima
                notaMaxima = Math.max(notaMaxima, nota);
                notaMinima = Math.min(notaMinima, nota);

                // Acumular notas para calcular la media
                sumaNotas += nota;
            }

            // Calcular media
            double media = sumaNotas / ASIGNATURAS;

            // Almacenar estadísticas en matrices correspondientes
            notaMaximaAlumno[i] = notaMaxima;
            notaMinimaAlumno[i] = notaMinima;
            mediaAlumno[i] = media;
        }

        // Mostrar las estadí­sticas almacenadas
        System.out.println("ASIGNATURAS:");
        System.out.println("");
        for (int j = 0; j < ASIGNATURAS; j++) {
            System.out.println("Asignatura " + (j + 1) + ":");
            System.out.println("  Nota máxima: " + notaMaximaAsignatura[j]);
            System.out.println("  Nota mí­nima: " + notaMinimaAsignatura[j]);
            System.out.println("  Media: " + mediaAsignatura[j]);
            System.out.println();
        }

        System.out.println("ALUMNOS:");
        System.out.println("");
        for (int i = 0; i < ALUMNOS; i++) {
            System.out.println("Alumno " + (i + 1) + ":");
            System.out.println("  Nota máxima: " + notaMaximaAlumno[i]);
            System.out.println("  Nota mí­nima: " + notaMinimaAlumno[i]);
            System.out.println("  Media: " + mediaAlumno[i]);
            System.out.println();
        }
    }
}
