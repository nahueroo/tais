from faster_whisper import WhisperModel
from utils import renombrar

# Faster-Whisper

def transcribir(nombreDelArchivo, ubicacion, duracion, nombre):
    model = WhisperModel(model_size_or_path="tiny", device="cpu")
    segments, info = model.transcribe(nombreDelArchivo, beam_size=5)

    print("Lenguaje detectado: '%s'. Probabilidad: '%f'" % (info.language, info.language_probability))

    for segment in segments:
        with open("%s/%s.txt" % (ubicacion,renombrar(nombre)), "a", encoding="utf-8") as f:
            print(f"{int((segment.end / duracion) * 100)}% completado.")
            f.write(segment.text)