# Samuel Gutiérrez Merino
# Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
# Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.
nota1 = float(input("Introduce tu nota de la primera calificación parcial: "));
nota2 = float(input("Introduce tu nota de la segunda calificación parcial: "));
nota3 = float(input("Introduce tu nota de la tercera calificación parcial: "));
notaexfinal = float(input("Introduce tu nota del examen final: "));
notatrabajo = float(input("Introduce tu nota del trabajo final: "));
notafinal = ((nota1 + nota2 + nota3)/3)*0.55 + notaexfinal*0.3 + notatrabajo*0.15;
print(f"Tu nota final es de {notafinal}")