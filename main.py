from faster_whisper import WhisperModel
from transformers import pipeline
from bajarVideos import bajarVideos
import os


currentfolder = os.getcwd()

# Pytubefix

url = input("Link: ")

ruta, path, videoRenombrado, duracion = bajarVideos(url)

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
