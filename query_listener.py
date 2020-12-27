import speech_recognition as sr
query=""
def takecommand():
    global query
    #it takes microphone input from user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        #r.pause_threshold =0.8
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-IN')
        print("user said:  ",query)

    except Exception as e:
        print(e)

        print("say that again please.......")
        query = ""
        return "None"
    return query

#takecommand()
def hindi():
    global query
    #it takes microphone input from user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        #r.pause_threshold =0.8
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='hi')
        print("user said:  ",query)

    except Exception as e:
        print(e)

        print("say that again please.......")
        query = ""
        return "None"
    return query
    

#hindi()
#hindi()

