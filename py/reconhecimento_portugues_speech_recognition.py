import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo...")

    # ajusta ruido no ambiente
    recon.adjust_for_ambient_noise(source)

    audio = recon.listen(source)

    # para usar outra chave de API -> 'recon.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")'
    # Usaremos chave de API (default) -> 'recon.recognize_google(audio)'

    # NOTE: Este exemplo requer PyAudio instalado para utilizar a classe Microphone

print(recon.recognize_google(audio, language='pt-BR'))