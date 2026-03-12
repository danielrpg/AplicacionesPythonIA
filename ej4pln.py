# https://www.nltk.org/ 
# especificamente para lenguages naturales

# hacer la descarga de un dato preentrenado
#import nltk
#nltk.download() # descarga todos
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

texto = """
    Bolivia esta cambiando debido a la tecnologia y la educacion.
    El gobierno esta implementando nuevas politicas para mejorar el pais.
    La gente esta mas informada y participativa.
    Definitivamente Bolivia esta cambiando.
"""
# tokenizacion por palabras
tokenizar = word_tokenize(texto)
# tokenizacion por oraciones
oraciones = sent_tokenize(texto)
# Eliminacion de palabras vacias
palabras_vacias = set(stopwords.words("spanish"))
resultadoPalabrasVacias = [palabra for palabra in tokenizar if palabra not in palabras_vacias]
print(tokenizar)
print(oraciones)
print(palabras_vacias)
print(resultadoPalabrasVacias)