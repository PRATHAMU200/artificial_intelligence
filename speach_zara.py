
import pyttsx3


engine = pyttsx3.init()
engine.runAndWait()
def speak_zara(a):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(a)
    engine.runAndWait()




