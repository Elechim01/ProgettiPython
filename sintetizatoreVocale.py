from gtts import gTTS, tts
from  playsound import playsound
import subprocess
text = """ ciao come va? test 2 
"""
tts = gTTS(text= text, lang='it')
tts.save("tts_output_audio.mp3")
print("Tutto fatto, file salvato")
playsound("tts_output_audio.mp3")
