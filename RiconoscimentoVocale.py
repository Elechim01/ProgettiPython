import speech_recognition as sr
recognizer_instance = sr.Recognizer()
"""
Per i file audio .wav 
wav = sr.AudioFile("")
with wav as source: 
    # lunghezza della pausa 
    recognizer_instance.pause_threshold = 3.0
"""
with sr.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    
    print("Sono in ascolto... Parla pure!")
    audio = recognizer_instance.listen(source)
    print("ok! sto elaborando il messaggio!")
try:
    text = recognizer_instance.recognize_google(audio, language= 'it-IT')
    print("Google ha capito \n",text)
except Exception as e:
    print(e)   

