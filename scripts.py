from videos import *
import os

def descargarVideos():
    url = input("Link:")
    video = obtenerVideo(url)
    print("Video obtenido")
    path = obtenerPathDescarga(video)
    print("Path obtenido")
    descargar(path, video)
    print("Video descargado")

def descargarPodcast():
    url = input("Link:")
    video = obtenerVideo(url)
    print(f"Video obtenido: {url}")
    path = obtenerPathPodcasts(video)
    print(f"Path obtenido: {path}")
    descargarParaPodcast(video, path)
    print(f"descargando {video} en {path}")
    print("Video descargado")


def transcribirVideos():
    from transcripcion import transcribir
    url = input("Link:")
    video = obtenerVideo(url)
    print(f"Video obtenido: {video.title}")
    path = obtenerPathTranscripcion(video)
    print(f"Path obtenido: {path}")
    audio = descargarParaTranscripcion(video, path)
    print("Video descargado")
    print(f"transcribiendo {audio} en {path}")
    transcribir(audio, path, video.length, video.title)