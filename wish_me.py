from speach import speak as spoke # for speaking use speak("enter text to speak")
from speach_zara import speak_zara # for speaking with zara use speak_zara("enter")
import datetime
def wishMe(speak_with):
    if speak_with == "zara" :
        speak = speak_zara
    else:
        speak = spoke



    
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
    speak("i am"+speak_with + " sir how may i help you")



