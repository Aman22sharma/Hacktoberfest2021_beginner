// AUTHOR: Avyay Jain
// Python3 Concept: (calculator)
// GITHUB: https://github.com/avyayjain

import pyttsx3
import speech_recognition as sr
import pywhatkit

engine = pyttsx3.init()

def speech(audio):
    engine.say(audio)
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print()
        print("Listening...")
        print()
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        print()    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        print()
        return "None"
    return query    

speech("what would you like to play ")
song = takeCommand()
speech('playing '+song)

pywhatkit.playonyt(song)

