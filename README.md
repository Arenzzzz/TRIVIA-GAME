Curador de preguntas (Arenz Peláez – 1556425)

Rol oficial: Diseñar, mantener y validar la base de datos de preguntas de la trivia.

Aportaciones concretas al proyecto:
Diseño de la estructura de datos:
Creó un diccionario de Python llamado preguntas que organiza las preguntas en distintos niveles de dificultad: FÁCIL, MEDIA, DIFÍCIL y EXTRAS.
Cada nivel contiene una lista de diccionarios individuales, con claves:
"Pregunta" → el enunciado.
"Respuesta" → la respuesta correcta.
"Opciones" → lista de cuatro posibles respuestas (una correcta y tres distractores).
Se aseguraron mínimo 10 preguntas por nivel principal para cumplir con los requisitos del proyecto.

Clasificación de preguntas:
Preguntas fáciles → conocimientos generales y cotidianos.
Preguntas medias → cultura general e historia.
Preguntas difíciles → matemáticas, ciencia y cultura más avanzada.
Preguntas extras → para la ronda de riesgo/recompensa, que suman o restan puntos.

Validación de entradas con la clase Validaciones:
Implementó una clase auxiliar para controlar la calidad de los datos ingresados cuando se agregan nuevas preguntas.
Métodos principales:
  espacios_vacios() → evita preguntas o respuestas en blanco.
  entrada_numerica() → asegura que la dificultad y opciones se seleccionen con números válidos.
  
Función agregar_preguntas():
Permite que el usuario registre nuevas preguntas dentro de la trivia.
Controla el flujo de:
  Selección del nivel de dificultad.
  Validación y normalización del texto de la pregunta (añadiendo signos de interrogación).
  Confirmación de que la respuesta correcta está incluida entre las opciones ingresadas.
Una vez validada, la pregunta se agrega al diccionario global preguntas.
Imprime un resumen de confirmación con el nivel, enunciado, respuesta correcta y opciones.

Contribución al crecimiento dinámico del juego:
Gracias a esta implementación, el juego no queda limitado a las preguntas predefinidas.
Los jugadores o futuros curadores pueden seguir alimentando la trivia con nuevas preguntas, manteniendo la dificultad organizada.
