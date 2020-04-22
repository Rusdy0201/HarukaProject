import os
import time
import speech_recognition as SR
import devControl
from gtts import gtts
from playsound import playsound as PS

def speak(audioString):
    print(audioString)
    tts = gTTS(text = audioString, lang = 'en')
    tts.save("speak.mp3")
    os.systems("mpg321 speak.mp3")
