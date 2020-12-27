from speach import speak as spoke # for speaking use speak("enter text to speak")

from speach_zara import speak_zara # for speaking with zara use speak_zara("enter")

from hindi_speak import speak_hindi

from wish_me import wishMe # for wishing use wishMe()

from security import security # for login into the jarvis

import query_listener  # the commands said by person (constant)

from camera import camera

from screenshot import screenshot

from translator_2 import translate 

import wikipedia
import webbrowser
import os
import datetime
import pyautogui
import keyboard
#Binary Files Complete
import pickle as p
import pywhatkit as kit
import datetime
from selenium import webdriver



speak_with = pyautogui.confirm("whom you want to speak with" , buttons = ["jarvis" , "zara"])

if speak_with == "zara" :
    speak = speak_zara
else:
    speak = spoke







def send(to,content):
    hour = int(datetime.datetime.now().hour)
    minu = int(datetime.datetime.now().minute)
    kit.sendwhatmsg(to,content,hour,minu+1)
    
def Search(l,con):
    try:
        f=open("STU.dat","rb")
        d={}
        fn=False
        try:
            while True:
                d=p.load(f)
                if d["nm"]==l:
                    send(d['num'],con)
                    fn=True
        except EOFError:
            f.close()
            if fn==False:
                speak("Record not found")
                print("Record Not Found")
    except FileNotFoundError:
        print("File Doesnot exists")
        speak("File Doesnot exists")

def group(a):
    l=a.split()
    lst=[]
    speak("message")
    query_listener.takecommand()
    con = query_listener.query
    con=con.lower()
    for i in range(3,len(l)):
        lst.append(l[i])
        top=len(lst)-1
    for i in range(top,-1,-1):
        Search(lst[i],con)
        


speak(" please login into your account")
print(" default username and password root ")
security()
speak("login succesfull")
print("login succesfull,,,,")






wishMe(speak_with)










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
    query = translate(query)
    query = query.lower()
    
    if "how are you" in query or "wassup" in query or "whatsup" in query:
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

    elif 'firefox' in query or 'mozilla' in query:
        path = "C:/Program Files/Mozilla Firefox/firefox.exe"
        url = "https://google.com"
        webbrowser.get(path).open(url)

    elif 'find' in query:

        elem = chromebrowser.find_element_by_name('p')  # Find the search box
        speak("what to find")
        
        elem.send_keys('seleniumhq' + Keys.RETURN)
        

    elif 'open stackoverflow' in query or 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")
        

#    elif 'open file' in query:
#        speak("enter file")
#        path = pyautogui.prompt("Enter path of file")
#        file = os.listdir(path)
#        print(file)
#        os.startfile(os.path.join(file))

   

        
    if 'search' in query:
        query=query.replace("search","")
        url = "https://www.google.com/search?q="+query 
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
        
        

    if 'time' in query:
        strTime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"sir, the time is {strTime}")
        print(f"sir, the time is {strTime}")
        
    if "send message" in query:
        group(query)

    elif "type" in query or "search" in query:
        query=query.replace("type","")
        keyboard.write(query)
        keyboard.press("enter")


    elif "enter" in query:
        keyboard.press("enter")

    elif "selfie" in query or "my photo" in query or "my image" in query or "capture image" in query:
        camera()

    elif "hindi" in query:
        speak_hindi(query)
        

    elif 'stop' in query:
        break

    else:
          print("say that again")
          query=""
            

    



    
    

