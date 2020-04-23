import os
import time
import speech_recognition as SR
import devControl as dv
from gtts import gTTS
from playsound import playsound as PS

def speak(audioString):
    print(audioString)
    tts = gTTS(text = audioString, lang = 'en')
    tts.save("speak.mp3")
    os.system("mpg321 speak.mp3")

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

    if "hi Haruka" in command:
        speak("hallo dad")
        PS("speak.mp3")

    if "where your mom" in command:
        speak("i don't know dad , maybe she was going out")
        PS("speak.mp3")

    elif "can you help me" in command:
        speak("of course dad , what can i do for you")
        PS("speak.mp3")



time.sleep(2)

while True:

    command = recordAudio()

    haruka(command)
