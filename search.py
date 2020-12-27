import wikipedia
import webbrowser
query=input("enter the query")
def webbrowser():
    global query
            
    if 'wikipedia' in query:
        speak('Searching Wikipedia....')
        query =query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        #webbrowser.open("youtube.com")
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query:
        #webbrowser.open("google.com")
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

webbrowser()


