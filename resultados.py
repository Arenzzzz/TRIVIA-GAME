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
    try:
        with open("puntajes.txt", "r") as archivo:
            lineas = archivo.readlines()
            if lineas:
                print("\nHistorial de puntajes:")
                for linea in lineas:
                    print(f"• {linea.strip()}")
            else:
                print("\nAún no hay puntajes registrados")
    except FileNotFoundError:
        print("\nEl archivo de puntaje no existe actualmente")
    except Exception as e:
        print(f"\nError existente al leer el historial: {e}")
