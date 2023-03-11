import psutil
import time
import keyboard
from colorama import init, Fore, Back, Style


def detener_script():
    global ejecutando
    ejecutando = False

# Asignar la función 'detener_script' a la tecla 'Enter'
keyboard.add_hotkey('enter', detener_script)

# Variable para controlar el bucle
ejecutando = True

print(Fore.LIGHTMAGENTA_EX + "! " + Fore.RESET + Fore.LIGHTWHITE_EX + "Press 'Enter' to stop the script.\n")

while ejecutando:
    memoria = psutil.virtual_memory()
    uso_memoria = memoria.used / 1024 / 102
    print(Fore.LIGHTGREEN_EX + "! " + Fore.RESET + Fore.LIGHTWHITE_EX + "The current use of RAM memory is {:.2f} MB".format(uso_memoria))
    time.sleep(1)

keyboard.remove_hotkey('enter')
