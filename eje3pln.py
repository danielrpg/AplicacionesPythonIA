import spacy 

# cargar el modelo en español 
pln = spacy.load("es_core_news_sm")

# Separacion de palabras
palabras = pln("Presidente Paz propone bloque de seis naciones para potenciar el desarrollo sudamericano en el 20 de Abril - 2026-04-01")

# cada palabra se puede tokenizar
for palabra in palabras.ents:
    print(palabra.text, palabra.label_)

# analisis gramatical
for palabra in palabras:
    print(palabra.text, palabra.pos_)

