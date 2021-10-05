//Author: Arayan Gupta
//Python concept: Spam Bot
//Github: https://github.com/Arayan1906
        
import pyautogui, time
time.sleep(5)
f=open("spam.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")




































