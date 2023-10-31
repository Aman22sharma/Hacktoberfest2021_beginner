# AUTHOR: homeboy445
# Python3 Concept: PDF to text and text narration
# GITHUB: https://github.com/homeboy445

'''
PDF reader:
Let your computer do the story telling!

How to get started?
Note: Make sure you have python installed 
in your system.

Linux: pip install pyttsx3 && pip install pdftotext && python3 Mainer.py
Windows: pip install pyttsx3, pip install pdftotext, python3 Mainer.py

Note: If this package "pdftotext" doesn't seem to work and/or you couldn't find it! please search online on how to install this on your respective machine...
'''

import pyttsx3
import pdftotext
from time import sleep

storyText = "Well, I am just a script and I don't think I can amuse you with a good story..."
storyText += "Just kidding......... I can, hahahahaha, but I think something's wrong with your pdf."
with open('story.pdf','rb') as pdfFile:
    try:
        pdf = pdftotext.PDF(pdfFile)
        storyText = ''
        for page in pdf:
            storyText += page
    except Exception as e:
        print(e)
        print("Oops, something went wrong")

speak = pyttsx3.init()
speak.say("Hello everyone! My name's ed and I am a nothing but a script!")
print("Hello everyone! My name's ed and I am a nothing but a script!")
speak.runAndWait()

ans = input("Did it worked (You heard him right?) ? (Y/N) ")
if ans == 'Y':
     speak.say("That's great!")
     print("That's great!")
     speak.runAndWait()
     sleep(2)
     speak.say("Let me tell you a story then... Let's go!")
     print("Let me tell you a story then... Let's go!")
     speak.runAndWait()
     sleep(2)
     speak.say(storyText)
     print(storyText)
     speak.runAndWait()
     sleep(3)
     speak.say("I'm hopefull that you enjoyed it!")
     print("I'm hopefull that you enjoyed it!")
     speak.runAndWait()
else:
    print("Try again maybe?")
