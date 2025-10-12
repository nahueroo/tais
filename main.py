from pytubefix import YouTube
from pytubefix.cli import on_progress
from faster_whisper import WhisperModel
from transformers import pipeline
from utils import renombrar
import os


currentfolder = os.getcwd()

# Pytubefix

url = input("Link: ")

video = YouTube(url, on_progress_callback = on_progress)
videoRenombrado = renombrar(video.title)
duracion = video.length

path = os.path.join(currentfolder, "transcripciones", f"{videoRenombrado}")

audio = video.streams.get_audio_only()
ruta = audio.download(path)

# Faster-Whisper

model = WhisperModel(model_size_or_path="small", device="cpu")
segments, info = model.transcribe(ruta, beam_size=5)

print("Lenguaje detectado: '%s'. Probabilidad: '%f'" % (info.language, info.language_probability))

for segment in segments:
    with open("%s/%s.txt" % (path, videoRenombrado), "a", encoding="utf-8") as f:
        print(f"{int((segment.end / duracion) * 100)}% completado.")
        f.write(segment.text)

# AI Summarize

procesadordetexto = pipeline("summarization", model="t5-small")

with open("%s/%s.txt" % (path,videoRenombrado)) as f:
    texto = f.read()

resumen = procesadordetexto(texto)

with open("%s/%s(resumen).txt" % (path,videoRenombrado), "w", encoding="utf-8") as f:
    f.write(resumen[0]['summary_text'])
