# CURADOR DE PREGINTAS
# Autor: ARENZ PELÁEZ - 1556425

preguntas = [
    {'FÁCIL':[
        {'¿Cuál es la capital de Francia?':{'Respuesta':'París', 'Opciones':['Madrid', 'París', 'Berlín', 'Roma']}},
        {'¿Cuánto es 2 + 2?':{'Respuesta':'4', 'Opciones':['1', '2', '3', '4']}},
        {'¿Qué animal dice "miau"?':{'Respuesta':'Gato', 'Opciones':['Gato', 'Perro', 'Gallina', 'Rana']}},
        {'¿Qué día sigue al Lunes?':{'Respuesta':'Martes', 'Opciones':['Miércoles', 'Domingo', 'Viernes', 'Martes']}},
        {'¿Cuántos meses tiene un año?':{'Respuesta':'12', 'Opciones':['10', '12', '11', '9']}},
        {'¿Cuál es el color de una manzana roja?':{'Respuesta':'Rojo', 'Opciones':['Rojo', 'Verde', 'Azul', 'Amarillo']}},
        {'¿Qué planeta es conocido como el planeta rojo?':{'Respuesta':'Marte', 'Opciones':['Tierra', 'Marte', 'Venus', 'Júpiter']}},
        {'¿Cuál es el número después del 9?':{'Respuesta':'10', 'Opciones':['10', '11', '8', '12']}},
        {'¿Qué gas respiramos principalmente?':{'Respuesta':'Oxígeno', 'Opciones':['Oxígeno', 'Hidrógeno', 'Nitrógeno', 'Helio']}},
        {'¿Cuál es la marca de tecnología con una manzana por logotipo?':{'Respuesta':'Apple', 'Opciones':['Tesla', 'Microsoft', 'Facebook', 'Apple']}}
        ]},
    {'MEDIA':[
        {'¿Cuál es el símbolo químico del oro?':{'Respuesta':'Au', 'Opciones':['Au', 'Ag', 'Go', 'O']}},
        {'¿Quién pintó la Mona Lisa?':{'Respuesta':'Da Vinci', 'Opciones':['Van Gogh', 'Picasso', 'Da Vinci', 'Rembrandt']}},
        {'¿Qué país tiene la mayor población?':{'Respuesta':'China', 'Opciones':['India', 'China', 'EEUU', 'Indonesia']}},
        {'¿Cuál es el océano más grande?':{'Respuesta':'Pacífico', 'Opciones':['Atlántico', 'Pacífico', 'Índico', 'Ártico']}},
        {'¿Cuál es la fórmula del agua?':{'Respuesta':'H20', 'Opciones':['H2O', 'CO2', 'O2', 'HO']}},
        {'¿En qué año llegó el hombre a la luna?':{'Respuesta':'1969', 'Opciones':['1965', '1969', '1972', '1960']}},
        {'¿Quién escribió "Cien años de soledad"?':{'Respuesta':'Gabriel García Márquez', 'Opciones':['Gabriel García Márquez', 'Pablo Neruda', 'Mario Vargas Llosa', 'Julio Cortázar']}},
        {'¿Cuál es el país más grande del mundo?':{'Respuesta':'Rusia', 'Opciones':['China', 'Estados Unidos', 'Rusia', 'Brasil']}},
        {'¿Qué elemento tiene el símbolo "O"?':{'Respuesta':'Oxígeno', 'Opciones':['Oro', 'Oxígeno', 'Plata', 'Ozono']}},
        {'¿Cuál es la raíz cuadrada de 144?':{'Respuesta':'12', 'Opciones':['10', '12', '14', '16']}}
        ]},
    {'DIFÍCIL':[
        {'¿Cuál es la derivada de x^2?':{'Respuesta':'x', 'Opciones':['x', '2x', 'x^2', '2']}},
        {'¿Qué elemento tiene número atómico 79?':{'Respuesta':'Oro', 'Opciones':['Oro', 'Plata', 'Plomo', 'Mercurio']}},
        {'¿Cuál es el valor de π hasta 2 decimales?':{'Respuesta':'3.14', 'Opciones':['3.12', '3.14', '3.15', '3.13']}},
        {'¿Qué teorema relaciona los catetos y la hipotenusa?':{'Respuesta':'Pitágoras', 'Opciones':['Pitágoras', 'Newton', 'Euclides', 'Tales']}},
        {'¿Quién formuló la teoría de la relatividad?':{'Respuesta':'Einstein', 'Opciones':['Newton', 'Einstein', 'Galileo', 'Tesla']}},
        {'¿Cuál es la integral de 2x dx?':{'Respuesta':'x^2 + C', 'Opciones':['x^2 + C', '2x^2 + C', 'x + C', 'x^2/2 + C']}},
        {'¿Qué país tiene la mayor densidad de población?':{'Respuesta':'Mónaco', 'Opciones':['Mónaco', 'India', 'China', 'Singapur']}},
        {'¿Cuál es la capital de Islandia?':{'Respuesta':'Reikiavik', 'Opciones':['Oslo', 'Reikiavik', 'Helsinki', 'Copenhague']}},
        {'¿Qué órgano produce la insulina?':{'Respuesta':'Páncreas', 'Opciones':['Hígado', 'Páncreas', 'Riñón', 'Corazón']}},
        {'¿Qué lenguaje se usa para programar páginas web?':{'Respuesta':'HTML', 'Opciones':['Python', 'HTML', 'C++', 'Java']}}
        ]},
    {'EXTRA':[
        {'¿Cuál es el país más pequeño del mundo?':{'Respuesta':'Ciudad del Vaticano', 'Opciones':['Mónaco', 'Ciudad del Vaticano', 'San Marino', 'Liechtenstein']}},
        {'¿Qué planeta del sistema solar tiene el día más largo?':{'Respuesta':'Venus', 'Opciones':['Mercurio', 'Venus', 'Marte', 'Júpiter']}},
        {'¿Cuál es el metal más ligero de todos?':{'Respuesta':'Litio', 'Opciones':['Aluminio', 'Magnesio', 'Litio', 'Titanio']}}
        ]}
]

# Clase para validar entradas de datos
class Validaciones:
    def __init__(self, dato):
        self.dato = dato

    # Métodos de validación de espacios vacíos
    def espacios_vacios(self):
        if not self.dato.strip():
            print('ERROR: Espacio en blanco')
            return False
        return True
    
    # Método de validación de entrada numérica (cuando se espera un número)
    def entrada_numerica(self):
        if not self.dato.isdigit():
            print('ERROR: Entrada no numérica')
            return False
        return True

# Función para agregar preguntas al registro
def agregar_preguntas():
    print('-' * 50); print('AGREGA TU PREGUNTA')
    niveles = []    # Lista para guardar las opciones de niveles de dificultad

    # Bucle para validar entrada de nivel de dificultad
    while True:
        # Impresión de opciones
        for i, tipo in enumerate(preguntas, 1):
            for nivel in tipo:
                niveles.append(nivel)
                print(f'{i}) {nivel}')
                
        dificultad = input('Dificultad: ')
        # Verificación de espacios en blanco y que sea número
        Validacion = Validaciones(dificultad)
        if Validacion.espacios_vacios() and Validacion.entrada_numerica():
            if 0 < int(dificultad) < len(niveles):
                # Se convierte la opcion de dificultad a texto
                dificultad = niveles[int(dificultad)-1]
                break
            else:
                print('ERROR: Nivel de dificultad inválido, intente de nuevo')
    
    # Bucle para validar entrada de pregunta
    while True:
        pregunta = input('Pregunta: ').capitalize().strip()
        
        # Verificación de espacios en blanco
        Validacion = Validaciones(pregunta)
        if Validacion.espacios_vacios():
            # Añadido de signos (¿?) si no se ingresan
            if not pregunta.startswith('¿'):
                pregunta = '¿' + pregunta
            if not pregunta.endswith('?'):
                pregunta = pregunta + '?'
            break
    
    # Bucle para validar el ingreso de respueta
    while True:
        respuesta = input('Respuesta: ')
        # Valida que se hayan ingresado datos
        if Validaciones(respuesta).espacios_vacios():
            break
    
    # Bucle para validar opciones
    while True:
        i = 1   # Contador de opciones
        opciones = []   # Lista para almacenar opciones ingresadas
        print('Agrega 4 opciones de respuesta')
        # Bucle para ingresar 4 opciones de respuesta
        while i <= 4:
            opcion = input(f'Opción {i}: ')
            # Verificación de espacios en blanco
            Validacion = Validaciones(opcion)
            if Validacion.espacios_vacios():
                # Se agregan las opciones a la lista y se aumenta el contador
                opciones.append(opcion)
                i += 1
    
        # Se verifica que se haya ingresado la respuesta dentro de las opciones
        if respuesta not in opciones:
            print('La respuesta no se encuentra en las opciones')
            opciones.clear()    # Se vacía la lista de opciones
        else:
            break
    
    question = {pregunta:{'Respuesta':respuesta, 'Opciones':opciones}}
    for tipo in preguntas:
        if dificultad in tipo:
            tipo[dificultad].append(question)

agregar_preguntas()