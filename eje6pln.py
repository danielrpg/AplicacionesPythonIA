# pip install python-telegram-bot

import spacy
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ContextTypes, filters, MessageHandler

procesamiento = spacy.load("es_core_news_sm")
token_telegram = "8794944975:AAHSIRsXdXVMwFfvSicomjaDHXdseeMvsNc"

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    doc = procesamiento(texto)
    palabras = [token.text for token in doc]
    
    # esta es la seccion de los activadores
    if "hola" in palabras:
        respuesta = "Hola bienvenido a UCATEC. En que puedo ayudarte?"
    elif "diplomado" in palabras:
        respuesta = "Tenemos 5 diplomados en Inteligencia Artificial"
    elif "precio" in palabras:
        respuesta = "El precio de los diplomados es de $1000"
    else:
        respuesta = "No entiendo tu pregunta"
    await update.message.reply_text(respuesta)


app= ApplicationBuilder().token(token_telegram).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot iniciado...")
app.run_polling()


