#Flujo general del programa
#A cargo de Luis Manuel carnet 1502325

import preguntas_y_respuestas
import random

def mostrar_pregunta(dificultad):
    InfoPregunta=preguntas_y_respuestas.preguntas[dificultad][random.randint(0,(len(preguntas_y_respuestas.preguntas[dificultad])-1))]
    pregunta=InfoPregunta['Pregunta']
    opciones=InfoPregunta['Opciones']
    respuesta=InfoPregunta["Respuesta"]
    print(pregunta)
    for i in range(1,5):
        print(f"{i}. {opciones[i-1]}")
    return respuesta