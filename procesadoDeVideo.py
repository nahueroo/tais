from transformers import pipeline

def procesarAudio(ubicacion, nombre):

    procesadordetexto = pipeline("summarization", model="t5-small")
    
    with open("%s/%s.txt" % (ubicacion,nombre)) as f:
        texto = f.read()
    
    resumen = procesadordetexto(texto)

    with open("%s/%s(resumen).txt" % (ubicacion,nombre), "w", encoding="utf-8") as f:
        f.write(resumen[0]['summary_text'])
