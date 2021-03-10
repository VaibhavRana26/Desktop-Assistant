import pyttsx3                                          # pysttsx3 - Text to Speech conversion Library
import datetime
import speech_recognition as sr                         # module to recognize speech input
import wikipedia
import webbrowser 
import os           

engine = pyttsx3.init('sapi5')                          #sapi5 = Speech Application Programming Interface for Windows 10 
voices = engine.getProperty('voices')   
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)               


def speak(audio):                                       #function to speak
    engine.say(audio)
    engine.runAndWait()

def wishMe():                                           #function to wish and welcome
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening") 
    speak("Hi I am Corona. How may I help you?")


def inputCommand():                                      # It takes microphone input from user and returns string output 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
   wishMe()

while True:
    query = inputCommand().lower()

       # Logic for executing tasks based on query
    if 'wikipedia' in query:
           speak("Searching Wikipedia...")
           query = query.replace('wikipedia','')
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia...")
           print(results)
           speak(results)
     
     
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
        
    elif 'open google' in query:
        webbrowser.open('google.com')

    elif 'open stackoverflow' in query:
        webbrowser.open('stackoverflow.com')
    
    elif 'play music' in query:
        music_dir = 'C:\\Users\\vaibh\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime('%H:%M:%S')
        print(strTime)
        speak(f'Sir, the time is: {strTime}') 

    else:
        break