import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="3390b364304a4ff99a78afc53fc4f439"



def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])



if __name__=="__main__":
    speak("Good evening sir how can i help you....")
    while True:
    #Listen for the wake word "jarvis"
    #obtain audio form the microphone
        r=sr.Recognizer()
        
        print("recognizing....")
        try:
           with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,timeout=5,phrase_time_limit=3)
           word=r.recognize_google(audio)
           if"jarvis" in word.lower():
                print("Wake word detected:", word)
                speak("Yes sir")
                #Listen for command
                with sr.Microphone() as source:
                    print("jarvis active....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)

                    
        except Exception as e:
            print("Error; {0}".format(e))