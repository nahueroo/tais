from pytubefix import YouTube
from pytubefix.cli import on_progress
from utils import renombrar
import os

def bajarVideos(url):

    video = YouTube(url, on_progress_callback = on_progress)
    videoRenombrado = renombrar(video.title)
    path = os.path.join(os.getcwd(), "transcripciones", f"{videoRenombrado}")
    audio = video.streams.get_audio_only()
    ruta = audio.download(path)
    duracion = video.length

    return ruta, path, videoRenombrado, duracion