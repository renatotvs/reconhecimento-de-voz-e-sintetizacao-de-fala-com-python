
import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:

    # ajusta ruido no ambiente
    recon.adjust_for_ambient_noise(source)

    while True:

        print("Descreva sua multiplicação: ")
        audio = recon.listen(source)

        resultadoFala = recon.recognize_google(audio, language="pt-BR")

        if resultadoFala == "fechar":
            print(resultadoFala)
            print("Fechando...")
            break
        else:
            print("Sua Multiplicação: " + str(resultadoFala))
            print("Resultado" + str(int(resultadoFala[0]) * int(resultadoFala[4])))

