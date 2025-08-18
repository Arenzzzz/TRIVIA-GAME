
# Proyecto: Propuesta 3 - Juego de Trivia con Puntajes

## Estudiantes

* De León González Alejandro Daniel – 1502425
* Velásquez González Luis Manuel – 1502325
* Pelaez Virula Moshé Arenz – 1556425
* Cholotío Mendoza Carlos Andrés – 1517925

## Descripción

Este proyecto consiste en el desarrollo de un juego de trivia en consola, donde los jugadores responden preguntas de selección múltiple clasificadas por nivel de dificultad.

El sistema:

* Asigna puntajes según la dificultad de cada pregunta.
* Ofrece una ronda extra opcional para ganar más puntos o perderlos si se falla.
* Permite registrar nuevas preguntas dinámicamente.
* Valida entradas para evitar errores en respuestas y registros.
* Guarda un historial de puntajes en un archivo para consulta posterior.

El trabajo se organizó con roles de equipo para fomentar la colaboración, el uso de GitHub y las buenas prácticas de programación en Python.


## Instrucciones de uso

1. Clonar el repositorio

   ```
   git clone https://github.com/Arenzzzz/TRIVIA-GAME.git
   cd TRIVIA-GAME
   ```

2. Ejecutar el juego
   Asegúrate de tener Python instalado y ejecuta:

   ```
   python main.py
   ```

3. Menú principal
   Al iniciar el programa, se mostrará un menú con opciones:

   * `1) Jugar` → Inicia una partida de trivia.
   * `2) Ver puntajes` → Muestra el historial de puntajes guardados en `puntajes.txt`.
   * `3) Agregar preguntas` → Permite ingresar nuevas preguntas al juego.
   * `4) Salir` → Cierra el programa.

4. Durante el juego

   * Ingresa tu nombre para comenzar.
   * Responde las preguntas seleccionando un número entre 1 y 4.
   * Al final de la partida, tu puntaje será guardado automáticamente.

5. Historial de puntajes

   * Todos los resultados se almacenan en el archivo `puntajes.txt`.
   * Puedes consultarlos desde la opción `2) Ver puntajes`.


## Roles de los Integrantes

### Curador de preguntas
**Arenz Peláez – 1556425**

* Diseñó y mantuvo la base de datos de preguntas.
* Clasificación por niveles: FÁCIL, MEDIA, DIFÍCIL y EXTRA.
* Implementó la clase **Validaciones** para asegurar la calidad de las preguntas nuevas.
* Función **agregar\_preguntas()** que permite registrar dinámicamente nuevas preguntas.
* Permite que el juego crezca con nuevas preguntas, manteniendo la dificultad organizada.

### Gestor de puntajes
**Alejandro de León – 1502425**

* Función **guardar\_puntaje(nombre, puntaje)** para almacenar resultados en `puntajes.txt`.
* Función **mostrar\_historial()** que lee y muestra todos los puntajes guardados.
* Manejo de errores con **try-except** para evitar fallos en lectura o escritura.
* Integración con el flujo del juego para registrar puntajes automáticamente al finalizar.

### Flujo general del programa
**Luis Manuel Velásquez – 1502325**

* Implementó el flujo principal del juego y la interacción con el usuario.
* Función **jugar()** que coordina la secuencia de preguntas según la dificultad y controla la ronda extra opcional.
* Función **mostrar\_pregunta(dificultad)** que selecciona aleatoriamente una pregunta de la base de datos y muestra sus opciones.
* Función **verificar\_respuesta(infoPregunta)** que valida la respuesta del jugador, asegurando entradas numéricas válidas y controlando errores.
* Función **agregar\_puntaje(dificultad, validez, puntaje)** que calcula y actualiza el puntaje de acuerdo a la dificultad y el resultado de la pregunta, incluyendo penalización para preguntas extras incorrectas.
* Creación del **menú principal**, permitiendo a los jugadores elegir entre jugar, ver puntajes, agregar preguntas o salir del programa.
* Integración con los módulos de **preguntas** y **resultados**, asegurando que las preguntas y los puntajes se gestionen correctamente.




## Conclusión

Este proyecto cumple con los requisitos de un juego funcional de trivia y fomenta:

* Trabajo colaborativo.
* Uso correcto de GitHub (commits, ramas, issues, documentación).
* Aplicación de estructuras de programación en Python (condicionales, ciclos, manejo de excepciones).

-

Si quieres, puedo también prepararte un **apartado de “Ejemplo de ejecución”** para agregar al final y que tu README se vea más completo. ¿Quieres que lo haga?
