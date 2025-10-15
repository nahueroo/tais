from pytubefix import YouTube
from pytubefix.cli import on_progress
from utils import renombrar
import os

def obtenerVideo(url):
    video = YouTube(url, on_progress_callback = on_progress)
    print(f"Video:{video.title}")
    return video

def renombradoVideo(video):
    return renombrar(video.title)

def obtenerPathDescarga(video):
    nombre = video.title
    return os.path.join(os.getcwd(), "descargas")

def obtenerPathTranscripcion(video):
    nombre = video.title
    return os.path.join(os.getcwd(), "transcripciones", f"{renombrar(nombre)}")

def obtenerPathPodcasts(video):
    nombre = video.title
    return os.path.join(os.getcwd(), "podcasts")

def obtenerPathTranscripcion(video):
    nombre = video.title
    return os.path.join(os.getcwd(), "transcripciones", f"{renombrar(nombre)}")

def descargarParaTranscripcion(video, path):
    stream = video.streams.get_audio_only()
    ruta = stream.download(path)
    return ruta

def descargarParaPodcast(video, path):
    stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()
    if(stream == None):
        stream = video.streams.get_audio_only()
    ruta = stream.download(path)
    return ruta

def descargar(path, video):

    stream = video.streams.filter(progressive=True).order_by("resolution").desc().first()

    if(stream != None):
        print("Audio y video juntos")
        path = stream.download(path)
    else:
        print("Audio y video separados")
        soloVideo = video.streams.get_by_resolution("1080p")
        if(soloVideo == None):
            soloVideo = video.streams.order_by("resolution").desc().first()

        ruta_video = soloVideo.download(path)
        soloAudio = video.streams.get_audio_only()
        ruta_audio = soloAudio.download(path)

def obtenerDuracion(video):
    return video.length