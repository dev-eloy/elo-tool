import os
import shutil
from colorama import init, Fore, Back, Style

# Definir las rutas de las carpetas temporales
rutas_temporales = [
    "C:\\Windows\\Temp",
]

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Inicializar los contadores
archivos_eliminados = 0
carpetas_eliminadas = 0
archivos_fallidos = 0
carpetas_fallidas = 0

limpiar_consola()
print()
for ruta in rutas_temporales:
    for nombre_archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, nombre_archivo)
        try:
            if os.path.isdir(ruta_archivo):
                shutil.rmtree(ruta_archivo, ignore_errors=True)
                print(Fore.LIGHTRED_EX + "! " + Fore.LIGHTBLACK_EX + "Deleted folder: " + ruta_archivo + Fore.RESET)
                carpetas_eliminadas += 1
            else:
                os.remove(ruta_archivo)
                print(Fore.LIGHTRED_EX + "! " + Fore.LIGHTBLACK_EX + "Deleted file: " + ruta_archivo + Fore.RESET)
                archivos_eliminados += 1
        except Exception as e:
            if os.path.isdir(ruta_archivo):
                carpetas_fallidas += 1
            else:
                archivos_fallidos += 1

# Mostrar los contadores
print(Fore.LIGHTGREEN_EX + "! " + Fore.RESET + Fore.LIGHTWHITE_EX + f"{archivos_eliminados} files and {carpetas_eliminadas} folders were deleted.")
print(Fore.LIGHTMAGENTA_EX + "! " + Fore.RESET + Fore.LIGHTWHITE_EX + f"{archivos_fallidos} files and {carpetas_fallidas} folders could not be deleted.")
print("")
