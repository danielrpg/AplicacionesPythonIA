# HABLAR - HABLANDO - HABLO - HABLADO =>  el modelo crea 4 diferentes tipos de entrenamiento
# RAMIFICACION DE PALABRAS

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

palabras = ["hablar", "hablando", "hablo", "hable", "hablado"]

for palabra in palabras:
    print(stemmer.stem(palabra))

# ahora en spanish 

from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer('spanish')

palabras = ["hablar", "hablando", "hablo", "hable", "hablado"]

for palabra in palabras:
    print(stemmer.stem(palabra))