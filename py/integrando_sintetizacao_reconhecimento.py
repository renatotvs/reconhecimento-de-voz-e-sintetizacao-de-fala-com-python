import pyttsx3 #para sintetizacao
import speech_recognition as sr #para reconhecimento da fala
import os #biblioteca do sistema

en = pyttsx3.init()
en.say("Olá senhor, você deseja ouvir sua música favorita? Responda sim ou caso contrário responda não.", {"voice":"luciana"})
en.setProperty('voice', b'brazil')
en.setProperty('rate', 140)
en.setProperty('volume', 1)
en.runAndWait()
en.stop()

#Reconhecimento da Fala
import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    audio = recon.listen(source)

    resposta = recon.recognize_google(audio, language="pt")
