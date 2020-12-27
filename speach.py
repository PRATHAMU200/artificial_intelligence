import pyttsx3
engine = pyttsx3.init()
engine.runAndWait()
def speak(a):
    engine.say(a)
    engine.runAndWait()


   

