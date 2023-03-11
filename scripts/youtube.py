import os
from pytube import YouTube
from colorama import init, Fore, Back, Style

# Ingresa el enlace del video de YouTube que quieres descargar
url = input(Fore.MAGENTA + "! " + Fore.LIGHTWHITE_EX + "Ingresa el enlace del video de YouTube: ")

# Crea una instancia de la clase YouTube
video = YouTube(url)

# Imprime información del video
print("")
print(Fore.YELLOW + "! " + Fore.LIGHTWHITE_EX + f"Title: {video.title}")
print(Fore.YELLOW + "! " + Fore.LIGHTWHITE_EX + f"Duration: {video.length} segundos")
print(Fore.YELLOW + "! " + Fore.LIGHTWHITE_EX + f"Average Mark: {video.rating}")
print(Fore.YELLOW + "! " + Fore.LIGHTWHITE_EX + f"Viewss: {video.views}")
print(Fore.YELLOW + "! " + Fore.LIGHTWHITE_EX + f"Description: " + Fore.LIGHTBLACK_EX + f"{video.description}" + Fore.RESET)

# Descarga el video en la calidad más alta disponible
video_stream = video.streams.get_highest_resolution()
video_path = video_stream.download()

# Obtiene la ruta de la carpeta donde se descargó el video
script_dir = os.path.dirname(os.path.abspath(__file__))
video_dir = os.path.join(script_dir, 'videos')

# Si la carpeta 'videos' no existe, se crea
if not os.path.exists(video_dir):
    os.makedirs(video_dir)

# Mueve el video descargado a la carpeta 'videos'
video_name = video.title + '.mp4'
video_path_new = os.path.join(video_dir, video_name)
os.rename(video_path, video_path_new)

print("")
print(Fore.GREEN + "! " + Fore.LIGHTWHITE_EX + "Download completed!")
print(Fore.GREEN + "! " + Fore.LIGHTWHITE_EX + f"The video was saved in the folder: {video_dir}")
print(Fore.GREEN + "! " + Fore.LIGHTWHITE_EX + f"File name: {video_name}")
