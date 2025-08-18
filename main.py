#Flujo general del programa
#A cargo de Luis Manuel carnet 1502325

import preguntas_y_respuestas   #Base de datos de preguntas
import random

#Función para mostrar una pregunta con sus opciones de forma aleatoria, guiandose por la dificultad
def mostrar_pregunta(dificultad):
    InfoPregunta=preguntas_y_respuestas.preguntas[dificultad][random.randint(0,(len(preguntas_y_respuestas.preguntas[dificultad])-1))]
    pregunta=InfoPregunta['Pregunta']
    opciones=InfoPregunta['Opciones']
    respuesta=InfoPregunta["Respuesta"]
    print(pregunta)
    for i in range(1,5):
        print(f"{i}. {opciones[i-1]}")
    return respuesta

#Función para verificar la respuesta
def verificar_respuesta(infoPregunta):
    respuesta_usuario=input("Tu respuesta en números: ")
    respuesta_usuario=int(respuesta_usuario)
    if 1<=respuesta_usuario<=4:
        if infoPregunta["Respuesta"]==infoPregunta["Opciones"][respuesta_usuario-1]:
            return True
        else:
            return False
    else:
        print ("La respuesta debe ser un número entre 1 y 4")

#función para agregar puntaje
def agregar_puntaje(dificultad, validez):
    if validez:
        if dificultad=="FÁCIL":
            puntaje+=1
        elif dificultad=="MEDIA":
            puntaje+=2
        elif dificultad=="DIFÍCIL":
            puntaje+=3
        elif dificultad=="EXTRA":
            puntaje+=2

def jugar():
    print(),print("*"*50)
    print("\n ¿Preparado para este reto?")
    nombre=input("Primero, dinos tu nombre: ").strip().title()
    puntaje=0
    while nombre=="":
        print("No trates de hacer trampa, ingresa un nombre válido")
        nombre=input("Ingresa tu nombre: ").strip().title()
    print(f"\n Ahora sí, demuestra lo que sabes {nombre}")
    
    dificultades=["FÁCIL", "MEDIA", "DÍFICIL"]
    for dificultad in dificultades:
        print(f"\nSe viene una pregunta {dificultad.lower()}")
        infoPregunta=mostrar_pregunta(dificultad)
        validez=verificar_respuesta(infoPregunta)

while True:
    print("\nBienvenidos a la mejor trivia del mundo")
    print("¿Qué deseas hacer?")
    print("1) Jugar")
    print("2) Ver puntajes")
    print("3) Agregar preguntas")
    print("4) Salir")
    opcion=input("Ingresa una opción: ")

    if opcion=="1":
        jugar()

    elif opcion=="2":
        #Función para mostrar los puntajes historicos
        pass
    elif opcion =="3":
        #Función para agregar preguntas
        pass
    elif opcion=="4":
        print("\n Gracias por usar nuestra trivia")
        print("Desarrollada por Alejandro, Arenz, Carlos y Manuel")
        print("Sigue aprendiendo...")
        break
    else:
        print("Opción no válida")