from videos import *
from transcripcion import transcribir
from procesadoDeVideo import procesarAudio
import os

def descargarVideos():
    url = input("Link:")
    video = obtenerVideo(url)
    print("Video obtenido")
    path = obtenerPathDescarga(video)
    print("Path obtenido")
    descargar(path, video)
    print("Video descargado")

def transcribirVideos():
    url = input("Link:")
    video = obtenerVideo(url)
    print("Video obtenido")
    path = obtenerPathTranscripcion(video)
    print("Path obtenido")
    audio = descargarSoloAudio(video, path)
    print("Video descargado")
    transcribir(audio, path, video.length)