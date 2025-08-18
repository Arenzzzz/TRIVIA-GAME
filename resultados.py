# resultados.py
# Este módulo se encargará de guardar y mostrar los puntajes del juego de trivia.
# Usaremos un archivo llamado 'puntajes.txt' para almacenar los resultados.

def guardar_puntaje(nombre, puntaje):
    try:
        print(f"{'Nombre':<10} | {'Puntaje'}")
        print("-" * 22)
        pass
    except Exception as e:
        print(f"Error existente al guardar el puntaje: {e}")
