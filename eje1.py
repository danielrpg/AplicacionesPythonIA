# pip install -U textblob
# python -m textblob.download_corpora

from textblob import TextBlob

texto = """
    La hamburguesa estaba horrible y no me gusto el servicio, 
    el mesero fue muy grosero y la comida estaba fria.
    Definitivamente no volveremos.
"""

analisis = TextBlob(texto)

print(analisis.sentiment)
# Rangos de polaridad
# Positivo: 1
# Negativo: -1
# Neutro: 0

# Rangos de subjetividad
# Objetivo: 0
# Neutro: 0.5
# Subjetivo: 1

print(f"Polaridad: {analisis.sentiment.polarity}")
print(f"Subjetividad: {analisis.sentiment.subjectivity}")

# if analisis.sentiment.polarity > 0.3:
#     print("Sentimiento Positivo")
# elif analisis.sentiment.polarity < -0.3:
#     print("Sentimiento Negativo")
# else:
#     print("Sentimiento Neutro")