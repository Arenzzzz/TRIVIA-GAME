# resultados.py
# Este módulo se encargará de guardar y mostrar los puntajes del juego de trivia.
# Usaremos un archivo llamado 'puntajes.txt' para almacenar los resultados.

def guardar_puntaje(nombre, puntaje):
    try:
        with open("puntajes.txt", "a") as archivo:
            print(f"{'Nombre':<10} | {'Puntaje'}")
            print("-" * 22)
            print(f"{nombre:<10} | {puntaje}", file=archivo)
    except Exception as e:
        print(f"Error existente al guardar el puntaje: {e}")

def mostrar_historial():
    # Esta función mostrará todos los puntajes guardados en puntajes.txt
    pass
