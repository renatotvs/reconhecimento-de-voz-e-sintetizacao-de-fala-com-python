
import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:

    while True:

        print("Descreva sua Operação: ")

        audio = recon.listen(source)

        resultadoOperacao = recon.recognize_google(audio, language="pt-BR")

        print("Operação: " + str(resultadoOperacao))

        if resultadoOperacao == "multiplicação":

            with sr.Microphone() as sourceMultiplicacao:

                print("Descreva sua Multiplicação: ")
                audioMultiplicacao = recon.listen(sourceMultiplicacao)
                resultadoMutltiplicacao = recon.recognize_google(audioMultiplicacao, language="pt-BR")

                print("Sua Multiplicação: " + str(resultadoMutltiplicacao))
                print("Resultado: " + str(int(resultadoMutltiplicacao[0]) * int(resultadoMutltiplicacao[4])))

        elif resultadoOperacao == "soma":

            with sr.Microphone() as sourceSoma:

                print("Descreva sua Soma: ")
                audioSoma = recon.listen(sourceSoma)
                resultadoSoma = recon.recognize_google(audioSoma, language="pt-BR")

                print("Sua Soma: " + str(resultadoSoma))
                print("Resultado: " + str(int(resultadoSoma[0]) * int(resultadoSoma[4])))

        elif resultadoOperacao == "fechar":
            print(resultadoOperacao)
            print("Fechando...")
            break
