# Samuel Gutiérrez Merino
# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que:
# por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
print ("El examen tiene 20 preguntas en total")
pregbien = float(input("Introduce la cantidad de preguntas que has respondido bien: "))
pregmal = float(input("Introduce la cantidad de preguntas que has respondido mal: "))
pregblanco = float(input("Introduce la cantidad de preguntas que has dejado en blanco: "))
nota = pregbien*5 + pregmal*(-1) + pregblanco*0
notafin = nota/10
print(f"Tu nota es {notafin}/10")