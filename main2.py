from videos import *
import os

url = input("Link:")

video = obtenerVideo(url)

print("Video obtenido")

path = obtenerPath(video)

print("Path obtenido")

descargarVideo(path, video)

print("Video descargado")