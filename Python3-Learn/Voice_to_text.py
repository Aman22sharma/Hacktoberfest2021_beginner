import speech_recognition as sr
Recognizer = sr.Recognizer()
with sr.Microphone as source:
    print("Speak Something")
    audio  = Recognizer.listen(source)
try:
    print("Your speech is:"+Recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("could not understand your speech")
except sr.RequestError as e:
    print("could not request results:;{}".format(e))
