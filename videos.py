from pytubefix import YouTube
from pytubefix.cli import on_progress
from utils import renombrar
import os

def obtenerVideo(url):
    return YouTube(url, on_progress_callback = on_progress)

def renombradoVideo(video):
    return renombrar(video.title)

def obtenerPath(video):
    nombre = video.title
    return os.path.join(os.getcwd(), "Descargas", f"{renombrar(nombre)}")

def descargarSoloAudio(video):
    return video.streams.get_audio_only()

def descargarVideo(path, video):

    stream = video.streams.filter(progressive=True).order_by("resolution").desc().first()

    if(stream != None):
        path = stream.download(path)
    else:
        soloVideo = video.streams.get_by_resolution("720p")
        if(soloVideo == None):
            soloVideo = video.streams.order_by("resolution").desc().first()

        ruta_video = soloVideo.download(path)
        soloAudio = video.streams.get_audio_only()
        ruta_audio = soloAudio.download(path)

def obtenerDuracion(video):
    return video.length