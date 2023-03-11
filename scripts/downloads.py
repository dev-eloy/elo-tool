import os
import shutil
from colorama import init, Fore, Back, Style

# Ruta a la carpeta Descargas del usuario actual
descargas = os.path.expanduser("~/Downloads")

# Contadores de archivos y carpetas eliminadas
num_archivos_eliminados = 0
num_carpetas_eliminadas = 0

# Recorre la carpeta Descargas eliminando archivos y carpetas
for elemento in os.listdir(descargas):
    ruta_elemento = os.path.join(descargas, elemento)
    if os.path.isfile(ruta_elemento):
        os.remove(ruta_elemento)
        print(Fore.RED + "! " + Fore.LIGHTBLACK_EX + f"Deleted file: {elemento}")
        num_archivos_eliminados += 1
    elif os.path.isdir(ruta_elemento):
        shutil.rmtree(ruta_elemento)
        print(Fore.RED + "! " + Fore.LIGHTBLACK_EX + f"Deleted folder: {elemento}")
        num_carpetas_eliminadas += 1

# Imprime el mensaje final
print(Fore.LIGHTGREEN_EX + "! " + Fore.LIGHTWHITE_EX + f"{num_archivos_eliminados} files and {num_carpetas_eliminadas} folders were deleted in the Downloads folder.")
print(Fore.LIGHTGREEN_EX + "! " + Fore.LIGHTWHITE_EX + "All files and folders in the Downloads folder have been deleted." + Fore.RESET)