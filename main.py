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

def recordAudio():
    r = SR.Recognizer()

    with SR.Microphone() as source:
        print("say something !")
        audio = r.listen(source)

    command = ""

    try:
        command = r.recognize_google(audio)
        print("you said: " + command)
    except SR.UnknownValueError:
        print("google speech recognition could not understand audio")
    except SR.RequestError as e:
        print("could not request result from google speech recognition service; {0}".format(e))

    return command

def haruka(command):

    if "hi" in command:
        speak("hallo")
        PS("speak.mp3")

    if "what is your name" in command:
        speak("my name is haruka")
        PS("speak.mp3")

    elif "who is your parents" in command:
        speak("her name is rusdiansyah")
        PS("speak.mp3")



time.sleep(2)

while True:

    command = recordAudio()

    haruka(command)
