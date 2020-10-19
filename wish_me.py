from speach import speak # for speaking use speak("enter text to speak")
import datetime
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning")
    elif hour>=0 and hour<6:
        speak("Good Night")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak ("sir..")
    speak("initializing databases , , initialing security setups , , i am online and ready sir ")
    speak("i am jarvis sir how may i help you")



