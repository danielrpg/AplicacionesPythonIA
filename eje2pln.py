#  pip install -U pip setuptools wheel
#  pip install -U spacy
# python -m spacy download es_core_news_sm
#
# python -m spacy download es_core_news_sm

import spacy

nlp = spacy.load("es_core_news_sm") # cargado del lenguage español

texto = """
    Bolivia esta cambiando debido a la tecnologia y la educacion.
    El gobierno esta implementando nuevas politicas para mejorar el pais.
    La gente esta mas informada y participativa.
    Definitivamente Bolivia esta cambiando.
"""

# doc = nlp(texto)

# for token in doc:
#     print(token.text, token.pos_, token.dep_)

analisis = nlp(texto)

for ent in analisis.ents:
    print(ent.text, ent.label_)