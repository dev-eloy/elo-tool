import os
from colorama import init, Fore, Back, Style

# Función para limpiar la consola
def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Bienvenida
limpiar_consola()
elotools = """
███████╗██╗      ██████╗       ████████╗ ██████╗  ██████╗ ██╗     
██╔════╝██║     ██╔═══██╗      ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
█████╗  ██║     ██║   ██║█████╗   ██║   ██║   ██║██║   ██║██║     
██╔══╝  ██║     ██║   ██║╚════╝   ██║   ██║   ██║██║   ██║██║     
███████╗███████╗╚██████╔╝         ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝╚══════╝ ╚═════╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝"""
print(Fore.LIGHTBLUE_EX + elotools + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "--------------------------" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "»» " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "Tools " + Fore.RESET + Fore.LIGHTWHITE_EX + "to optimize your workspace and obtain information about your PC, also for other things " + Fore.RESET + Fore.LIGHTMAGENTA_EX +  " ⊹╰ (⌣ʟ⌣) ╯⊹" + Fore.RESET )
input(Fore.LIGHTBLACK_EX + "»» " + Fore.RESET + Fore.LIGHTWHITE_EX + "Press Enter to continue...")

# Bucle principal del menú
while True:
    # Mostrar el menú de opciones
    limpiar_consola()
    print(Fore.LIGHTBLUE_EX + elotools + Fore.RESET)
    print(Fore.LIGHTBLACK_EX + "→ " + Fore.RESET + Fore.LIGHTGREEN_EX + "Select a option:")
    print(Fore.LIGHTBLACK_EX + "»» " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "1." + Fore.RESET + Fore.LIGHTWHITE_EX + " Delete temporary files")
    print(Fore.LIGHTBLACK_EX + "»» " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "2." + Fore.RESET + Fore.LIGHTWHITE_EX + " Empty the recycling bin")
    print(Fore.LIGHTBLACK_EX + "»» " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "3." + Fore.RESET + Fore.LIGHTWHITE_EX + " Check RAM Memory usage")
    print(Fore.LIGHTBLACK_EX + "»» " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "4." + Fore.RESET + Fore.LIGHTWHITE_EX + " Get detailed information about your CPU and system")
    print(Fore.LIGHTBLACK_EX + "»» " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "5." + Fore.RESET + Fore.LIGHTWHITE_EX + " Delete Downloads")
    print(Fore.LIGHTBLACK_EX + "»» " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "6." + Fore.RESET + Fore.LIGHTWHITE_EX + " Download youtube videos")

    print(Fore.LIGHTBLACK_EX + "»» " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "0." + Fore.RESET + Fore.LIGHTWHITE_EX + " Exit")

    opcion = input(Fore.LIGHTBLACK_EX + "»» " + Fore.LIGHTWHITE_EX + "Option: " + Fore.RESET)

    if opcion == "1":
        limpiar_consola()
        exec(open("scripts/temp.py").read())
    elif opcion == "2":
        limpiar_consola()
        exec(open("scripts/recycle-bin.py").read())
    elif opcion == "3":
        limpiar_consola()
        exec(open("scripts/ram.py").read())
    elif opcion == "4":
        limpiar_consola()
        exec(open("scripts/system.py").read())
    elif opcion == "5":
        limpiar_consola()
        exec(open("scripts/downloads.py").read())
    elif opcion == "6":
        limpiar_consola()
        exec(open("scripts/youtube.py").read())
    elif opcion == "0":
        break
    else:
        print("Invalid option. Try again.")
    
    respuesta = input(Fore.LIGHTBLACK_EX + "! " + Fore.RESET + Fore.LIGHTWHITE_EX + "Press 'Enter' to return to the menu, or type 'Exit' to end the program: " + Fore.RESET)
    limpiar_consola()
    if respuesta.lower() == "exit":
        break

