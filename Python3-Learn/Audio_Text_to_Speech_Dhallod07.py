'''
AUTHOR: Ankush Dhallod
Python3 Concept: Text to speech in Python
GITHUB: https://www.github.com/Dhallod07
'''

#pip install pyttsx3
#This Library is used for TEXT TO SPEECH

import pyttsx3

speaker = pyttsx3.init()

# Sets speed percent
# Can be more than 100
speaker.setProperty('rate', 120)

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# Use female voice
speaker.setProperty('voice', voice_id)
speaker.say("Hello I can speak as well")
speaker.runAndWait()