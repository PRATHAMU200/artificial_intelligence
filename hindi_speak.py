# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os
from playsound import playsound
from translator_2 import translate_hindi


def speak_hindi(query):
    mytext = translate_hindi(query)

# The text that you want to convert to audio 


# Language in which you want to convert 
    language = 'hi'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
    myobj.save("welcome.mp3")


# Playing the converted file 
    playsound(os.getcwd()+"\welcome.mp3")

speak_hindi("how are you")
