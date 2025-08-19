#Flujo general del programa
#A cargo de Luis Manuel carnet 1502325

import preguntas   #Banco de preguntas
import random
import resultados       #Base de datos para el historial de puntajes

#Función para mostrar una pregunta con sus opciones de forma aleatoria, guiandose por la dificultad
def mostrar_pregunta(dificultad):
    InfoPregunta=preguntas.preguntas[dificultad][random.randint(0,(len(preguntas.preguntas[dificultad])-1))]        #Extraer pregunta del banco de preguntas
    pregunta=InfoPregunta['Pregunta']    #Dividirla en pregunta, ocpiones y respuesta para su uso
    opciones=InfoPregunta['Opciones']
    respuesta=InfoPregunta["Respuesta"]
    print(pregunta)
    for i in range(1,5):
        print(f"{i}. {opciones[i-1]}")
    return InfoPregunta

#Función para verificar la respuesta
def verificar_respuesta(infoPregunta):
    comprobacion=False
    while comprobacion==False:   #Ciclo for hasta ingresar pregunta válida 
        respuesta_usuario=input("Tu respuesta en números: ")
        try:    #Comrpobar si es respuesta válida
            respuesta_usuario=int(respuesta_usuario)
            if 1<=respuesta_usuario<=4:
                if infoPregunta["Respuesta"]==infoPregunta["Opciones"][respuesta_usuario-1]:    #Comprobar si es la respuesta correcta
                    comprobacion=True    #Terminar el bucle
                    return True            #retornar la validez de la respuesta
                else:
                    comprobacion=True    #Terminar el bucle
                    return False        #Retornar la validez de la respuesta
            else:
                raise ValueError ("La respuesta debe ser un número entre 1 y 4")
        except ValueError as e:
            print("Error:", e)

#función para agregar puntaje
def agregar_puntaje(dificultad, validez, puntaje):
    if validez:
        if dificultad=="FÁCIL":
            puntaje+=1
        elif dificultad=="MEDIA":
            puntaje+=2
        elif dificultad=="DIFÍCIL":
            puntaje+=3
        elif dificultad=="EXTRAS":
            puntaje+=2
    elif validez==False and dificultad=="EXTRAS":
        puntaje-=3
    return puntaje

def jugar():
    print(),print("*"*35)
    print("¿Preparado para este reto?")
    nombre=input("Primero, dinos tu nombre: ").strip().title()
    puntaje=0
    while nombre=="":    #Comprobación nombre
        print("No trates de hacer trampa, ingresa un nombre válido")
        nombre=input("Ingresa tu nombre: ").strip().title()
    print(f"\nAhora sí, demuestra lo que sabes {nombre}")
    
    dificultades=["FÁCIL", "MEDIA", "DIFÍCIL"]

    #Ciclo for para pasar una pregunta de cada tipo
    for dificultad in dificultades:
        print(f"\nSe viene una pregunta {dificultad.lower()}")
        infoPregunta=mostrar_pregunta(dificultad)
        validez=verificar_respuesta(infoPregunta)
        puntaje=agregar_puntaje(dificultad,validez,puntaje)

    print(f"\nTerminaste la ronda con {puntaje} puntos, pero puedes seguir jugando")
    print("Responde una pregunta extra por 2 puntos más, pero si te equivocas pierdes 3 puntos")
    pregunta_extra=input("¿Deseas la pregunta? escribe 'si' para darte la pregunta o un enter para terminar: ")
    if pregunta_extra=="si":
        print("\nSe viene una pregunta extra, aquí se define todo")
        infoPregunta=mostrar_pregunta("EXTRAS")
        validez=verificar_respuesta(infoPregunta)
        puntaje=agregar_puntaje("EXTRAS", validez, puntaje)

    print(f"\n-Muy bien {nombre}")
    print(f"Obtuviste un total de {puntaje} puntos")

    #guardar datos
    print("Guardando tus datos...")
    resultados.guardar_puntaje(nombre, puntaje)

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
        resultados.mostrar_historial()      #Función para mostrar los puntajes historicos
        
    elif opcion =="3":
        preguntas.agregar_preguntas()       #Función para agregar preguntas

    elif opcion=="4":
        print("\n Gracias por usar nuestra trivia")
        print("Desarrollada por Alejandro, Arenz, Carlos y Manuel")
        print("Sigue aprendiendo...")
        break
    else:
        print("Opción no válida")
