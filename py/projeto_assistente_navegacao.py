import pyttsx3  # para sintetização
import speech_recognition as sr  # para reconhecimento de vóz
import webbrowser  # para manipulação do brownser

# sintetização
en = pyttsx3.init()
en.say("Olá senhor, o que deseja fazer nesse momento?")
en.setProperty('voice', b'brazil')
en.setProperty('rate', 180)
en.setProperty('volume', 1)
en.runAndWait()
en.stop()

# reconhecimento da fala
recon = sr.Recognizer()

with sr.Microphone() as source:
    print("Fale o que deseja...")

    audio = recon.listen(source)

    respAudio = recon.recognize_google(audio, language='pt-BR')

    print(respAudio)

    if respAudio == "Google":
        en.say("abrindo o Google")
        en.setProperty('voice', b'brazil')
        en.setProperty('rate', 180)
        en.setProperty('volume', 1)
        en.runAndWait()

        webbrowser.open("http://www.google.com.br")

    else:

        en.say("Me desculpe, não compreendi. Tente novamente.")
        en.setProperty('voice', b'brazil')
        en.setProperty('rate', 180)
        en.setProperty('volume', 1)
        en.runAndWait()
        en.stop()
