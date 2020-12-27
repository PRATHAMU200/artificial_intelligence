from speach import speak # for speaking use speak("enter text to speak")

from wish_me import wishMe # for wishing use wishMe()

from security import security # for login into the jarvis

import query_listener  # the commands said by person (constant)

from screenshot import screenshot

import wikipedia
import webbrowser
import os
import datetime
import pyautogui







speak(" please login into your account")
print(" default username and password root ")
security()
speak("login succesfull")
print("login succesfull,,,,")






wishMe()










# functions for operational settings


def add():
      a= query
      lst=[]
      for i in a.split():
            if i.isdigit():
                  lst+=[int(i)]
      d=sum(lst)
      print(d)
def sub():
      a= query
      lst=[]
      for i in a.split():
            if i.isdigit():
                  lst+=[int(i)]
      if len(lst)==2:
            print(lst[1]-lst[0])
      else:
            print("subtraction requires only two operands")
      
def mul():
      s=1
      a= query
      lst=[]
      for i in a.split():
            if i.isdigit():
                  lst+=[int(i)]
      for i in lst:
            s*=i
      print(s)
def div():
      a= query
      lst=[]
      for i in a.split():
            if i.isdigit():
                  lst+=[int(i)]
      if len(lst)==2:
            if lst[1]!=0:
                  print(lst[0]/lst[1])
            else:
                  print("divide by zero!")
      else:
            print("division requires only two operands")









#main program starts here
while True:            
    query_listener.takecommand()
    query = query_listener.query
    query = query.lower()
    
    if "how are you" in query:
          speak("fine sir,")

          
    elif "division" in query or "divide" in query:
          div()

          
    elif "multiply" in query:
          mul()

          
    elif "add" in query:
          speak("ok sir")
          add()

          
    elif "subtract" in query or "subtraction" in query or "substract" in query:
          sub()

          
    elif "screenshot" in query:
          speak("taking screenshot")
          speak("please enter path")
          screenshot()
          speak("screenshot has been saved")
          


    elif 'wikipedia'  in query:
        speak('Searching Wikipedia....')
        query =query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
        
    elif 'open youtube' in query:
        speak("opening youtube")
        #webbrowser.open("youtube.com")
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        

    elif 'open google' in query:
        speak("opening google")
        #webbrowser.open("google.com")
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        

    elif 'open stackoverflow' in query or 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")
        

#    elif 'open file' in query:
#        speak("enter file")
#        path = pyautogui.prompt("Enter path of file")
#        file = os.listdir(path)
#        print(file)
#        os.startfile(os.path.join(file))
        
    elif 'search for' in query:
        url = query 
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
        

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"sir, the time is {strTime}")
        print(f"sir, the time is {strTime}")
        

    elif 'stop' in query:
        break

    else:
          print("say that again")
          query=""
            

    



    
    

