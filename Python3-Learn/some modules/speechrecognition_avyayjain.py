import speech_recognition as sr
import datetime as dt

def recognisation():
 r=sr.Recognizer()
 print(sr.Microphone.list_microphone_names())
 with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
    print("say anything : ")
    audio= r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("sorry, could not recognise")



b= recognisation()
print(b)

