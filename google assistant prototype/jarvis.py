import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source) #reduce noise
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mohitchoudhary1054@gmail.com', '############')
    server.sendmail('mohitchoudhary1054@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'open whatsapp web' in query:
            webbrowser.open("https://web.whatsapp.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'open email' in query:
            webbrowser.open("E-mail.com")
        elif 'open spotify' in query:
            webbrowser.open('httpd://wwwspotify.com')    
        elif 'play ' in query:
            anime_dir = 'C:\\Users\\DELL 5510\\Downloads\\Telegram Desktop'
            songs = os.listdir(anime_dir)
            print(songs)    
            os.startfile(os.path.join(anime_dir, songs[0]))
        elif 'open vs' in query:
            o = 'C:\\Users\\DELL 5510\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(os.path.join(o))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'search' in query:
            speak(f"")    
        elif 'who are you' in query :    
            speak(f"sir , i am jarvis.I am a software made by you")
            
        elif 'repeat after me' in query:
            speak(f"what should i say")  
            content = takeCommand()
            speak(f"{content}")  
        elif 'open code' in query:
            codePath = "C:\\project"
            os.startfile(codePath)    
        elif 'who am i' in query:
            speak(f"You are Mohit Choudhary, You are the one who created me ")
        elif 'look for' in query:
            speak('what should i search ')
            content = takeCommand()
            webbrowser.open("{content}")   
        elif 'go' in query:
            break;     
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "wrhndsunita@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
    