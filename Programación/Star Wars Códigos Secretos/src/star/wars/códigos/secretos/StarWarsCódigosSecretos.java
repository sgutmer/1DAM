/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package star.wars.códigos.secretos;
import java.util.Scanner;
import java.util.InputMismatchException;
/**
 *
 * @author Francisco Jiménez Álvarez
 */
public class StarWarsCódigosSecretos {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        //Variables
        Scanner sc=new Scanner(System.in);
        boolean perder=false;
        int nivel=1;
        String intro;
        int S1=(int)(Math.random()*10+1);
        int S2=(int)(Math.random()*11+20);
        int P1=(int)(Math.random()*7+1);
        int P2=(int)(Math.random()*5+8);
        int N=(int)(Math.random()*51+50);
        int P=(int)(Math.random()*91+10);
        int M=(int)(Math.random()*6+5);
        int S=(int)(Math.random()*6+5);
        int factorialM=1;
        int factorialS=1;
        boolean primo = true;
        int solucion=0;
        int respuesta;
        
        //Mostrar inicio
        System.out.println("\u001B[33m=== STAR WARS CÓDIGOS SECRETOS ===\n" +
        "Hace mucho tiempo, en una galaxia muy, muy lejana… La Princesa Leia, Luke\n" +
        "Skywalker, Han Solo, Chewbacca, C3PO y R2D2 viajan en una nave imperial robada\n" +
        "en una misión secreta para infiltrarse en otra estrella de la muerte que el imperio\n" +
        "está construyendo para destruirla. (Presiona Intro para continuar)");
        
        //Seguir con un INTRO
        intro=sc.nextLine();
        
        //Bucle para seguir mientras nivel no sea 6
        do {       
            
        //Switch de niveles
        switch (nivel) {
            case 1:
                
                //Mostrar nivel 1
                System.out.println("\n\u001B[36m=== NIVEL 1 ===\n" +
                "Los problemas empiezan cuando deben realizar un salto hiperespacial hasta al\n" +
                "sistema "+S1+" en el sector "+S2+", pero el sistema de navegación está estropeado y el\n" +
                "computador tiene problemas para calcular parte de las coordenadas de salto.\n" +
                "Chewbacca, piloto experto, se da cuenta que falta el cuarto número de la serie.\n" +
                "Recuerda de sus tiempos en la academia de pilotos que para calcularlo hay que\n" +
                "calcular el sumatorio entre el nº del sistema y el nº del sector (ambos inclusive).\n" +
                "¿Qué debe introducir?\n");
                
                //Bucle para el sumatorio
                for (int i = S1; i <= S2; i++) {
                    solucion+=i;
                }
                
                try {
                    //Preguntamos al usuario
                    respuesta = sc.nextInt();
                    
                    //Comprobar respuestas y pasar nivel o salir
                    if (respuesta==solucion){
                        nivel=2;
                    }else{
                        perder=true;
                        nivel=6;
                    }
                } catch (InputMismatchException e) {
                    System.out.println("\u001B[31mERROR!! Tenías que incluir un número entero");
                    perder=true;
                    nivel=6;
                }
                
                //Resetear variables a 0
                solucion=0;
                respuesta=0;
                break;
                
            case 2:
                
                //Mostrar nivel 2
                System.out.println("\n\u001B[36m=== NIVEL 2 ===\n" +
                "Gracias a Chewbacca consiguen llegar al sistema correcto y ven a lo lejos la estrella\n" +
                "de la muerte. Como van en una nave imperial robada se aproximan lentamente con\n" +
                "la intención de pasar desapercibidos. De repente suena el comunicador. “Aquí\n" +
                "agente de espaciopuerto "+P1+" contactando con nave imperial "+P2+". No están destinados\n" +
                "en este sector. ¿Qué hacen aquí?”. Han Solo coge el comunicador e improvisa.\n" +
                "“Eh… tenemos un fallo en el… eh… condensador de fluzo... Solicitamos permiso\n" +
                "para atracar y reparar la nave”. El agente, que no se anda con tonterías, responde\n" +
                "“Proporcione código de acceso o abriremos fuego”. Han Solo ojea rápidamente el\n" +
                "manual del piloto que estaba en la guantera y da con la página correcta. El código\n" +
                "es el productorio entre el nº del agente y el nº de la nave (ambos inclusive).\n" +
                "¿Cuál es el código?\n");
                
                //Inicializar el productorio a P1
                solucion=P1;
                
                //Bucle para calcular productorio
                for (int i = P1+1; i <= P2; i++) {
                    solucion=solucion*i;
                }
                
                try {
                    //Respuesta del usuario
                    respuesta=sc.nextInt();

                    //Comprobar respuestas y pasar nivel o salir
                    if (respuesta==solucion){
                        nivel=3;
                    }else{
                        perder=true;
                        nivel=6;
                    }
                
                } catch (InputMismatchException e) {
                    System.out.println("\u001B[31mERROR!! Tenías que incluir un número entero");
                    perder=true;
                    nivel=6;
                }
                
                //Resetear variables a 0
                solucion=0;
                respuesta=0;
                break;
                
            case 3:
                
                //Mostrar Nivel 3
                System.out.println("\n\u001B[36m=== NIVEL 3 ===\n" +
                "Han Solo proporciona el código correcto. Atracan en la estrella de la muerte, se\n" +
                "equipan con trajes de soldados imperiales que encuentran en la nave para pasar\n" +
                "desapercibidos y bajan. Ahora deben averiguar en qué nivel de los "+N+" existentes se\n" +
                "encuentra el reactor principal. Se dirigen al primer panel computerizado que\n" +
                "encuentran y la Princesa Leia intenta acceder a los planos de la nave pero necesita\n" +
                "introducir una clave de acceso. Entonces recuerda la información que le proporcionó\n" +
                "Lando Calrissian “La clave de acceso a los planos de la nave es el factorial de "+N+"/10\n" +
                "(redondeando "+N+" hacia abajo), donde "+N+" es el nº de niveles”.\n" +
                "¿Cual es el nivel correcto?\n");
                
                //Inicializar solución a 1 para hacer el factorial
                solucion=1;
                
                //Dividir N entre 10
                N=(N/10);
                
                //Calcular factorial de N
                for (int i = 1; i <= N; i++) {
                    solucion=solucion*i;
                }
                
                try {
                    //Respuesta del usuario
                    respuesta=sc.nextInt();

                    //Comprobar respuestas y pasar nivel o salir
                    if (respuesta==solucion){
                        nivel=4;
                    }else{
                        perder=true;
                        nivel=6;
                    }
                
                } catch (InputMismatchException e) {
                    System.out.println("\u001B[31mERROR!! Tenías que incluir un número entero");
                    perder=true;
                    nivel=6;
                }
                
                //Resetear variables a 0
                solucion=0;
                respuesta=0;
                
                break;
                
            case 4:
                
                //Mostrar Nivel 4
                System.out.println("\n\u001B[36m=== NIVEL 4 ===\n" +
                "Gracias a la inteligencia de Leia llegan al nivel correcto y encuentran la puerta\n" +
                "acorazada que da al reactor principal. R2D2 se conecta al panel de acceso para\n" +
                "intentar hackear el sistema y abrir la puerta. Para desencriptar la clave necesita\n" +
                "verificar si el número "+P+" es primo o no. Si es primo introduce un 1, si no lo es\n" +
                "introduce un 0.\n");
                
                //Bucle para comprobar si el P es primo
                for (int i = 2; i <= Math.sqrt(P); i++) {
                    if (P%i == 0) {
                        primo = false;
                    }
                }

                //Asignar solución dependiendo si es primo o no
                if (primo) {
                    solucion=1;
                }
                else
                    solucion=0;
                
                try {
                    //Respuesta del usuario
                    respuesta=sc.nextInt();

                    //Comprobar respuestas y pasar nivel o salir
                    if (respuesta==solucion){
                        nivel=5;
                    }else{
                        perder=true;
                        nivel=6;
                    }
                
                } catch (InputMismatchException e) {
                    System.out.println("\u001B[31mERROR!! Tenías que incluir un número entero");
                    perder=true;
                    nivel=6;
                }
                
                //Resetear variables a 0
                solucion=0;
                respuesta=0;
                
                break;
                
            case 5:
                
                //Mostrar Nivel 5
                System.out.println("\n\u001B[36m=== NIVEL 5 ===\n" +
                "Consiguen entrar al reactor. Ya solo queda que Luke Skywalker coloque la bomba,\n" +
                "programe el temporizador y salir de allí corriendo. Necesita programarlo para que\n" +
                "explote en exactamente "+M+" minutos y "+S+" segundos, el tiempo suficiente para escapar\n" +
                "antes de que explote pero sin que el sistema de seguridad anti-explosivos detecte y\n" +
                "desactive la bomba. Pero el temporizador utiliza un reloj Zordgiano un tanto\n" +
                "peculiar. Para convertir los minutos y segundos al sistema Zordgiano hay que sumar\n" +
                "el factorial de "+M+" y el factorial de "+S+". ¿Qué valor debe introducir?\n");
                
                //Calcular factorial de N
                for (int i = 1; i <= M; i++) {
                    factorialM=factorialM*i;
                }
                
                //Calcular factorial de N
                for (int i = 1; i <= S; i++) {
                    factorialS=factorialS*i;
                }
                
                //Calcular solución sumando los dos factoriales
                solucion=factorialM+factorialS;
                
                try {
                    //Respuesta del usuario
                    respuesta=sc.nextInt();

                    //Comprobar respuestas y pasar nivel o salir
                    if (respuesta==solucion){
                        nivel=6;
                    }else{
                        perder=true;
                        nivel=6;
                    }
                
                } catch (InputMismatchException e) {
                    System.out.println("\u001B[31mERROR!! Tenías que incluir un número entero");
                    perder=true;
                    nivel=6;
                }
                
                break;
        }
        
        } while (nivel<6);
        
        //Pantallas Finales
        
        //Pantalla Derrota
        if (perder) {
            System.out.println("\nEse no era el código correcto… La misión ha sido un fracaso… :( :( :(\n" +
            "Todavía no eres un Maestro Jedi de las Matemáticas. ¡Vuelve a intentarlo!");
        }
        //Pantalla Victoria
        else{
            System.out.println("\nLuke Skywalker introduce el tiempo correcto, activa el temporizador y empiezan a\n" +
            "sonar las alarmas. Salen de allí corriendo, no hay tiempo que perder. La nave se\n" +
            "convierte en un hervidero de soldados de arriba a abajo y entre el caos que les rodea\n" +
            "consiguen llegar a la nave y salir de allí a toda prisa. A medida que se alejan\n" +
            "observan por la ventana la imagen de la colosal estrella de la muerte explotando en\n" +
            "el silencio del espacio, desapareciendo para siempre junto a los restos del malvado\n" +
            "imperio.\n" +
            "¡Has salvado la galaxia gracias a la Fuerza Jedi de las matemáticas! Enhorabuena ;D");
        }
        
        //FINAL
        System.out.println("\n\u001B[35mGracias por jugar :D");
    }
    
}
