// AUTHOR: Aman
// Python3 Concept: datetime module and speech module
// GITHUB: https://github.com/amansaini01
    
    
    
import pyttsx3
import datetime
import time


# speaking function
spk = pyttsx3.init()
voices = spk.getProperty('voices')
spk.setProperty('voice', voices[2].id)

def speak(voice):
    spk.say(voice)
    spk.runAndWait()

    
    
    
# wishing function
def wishMe():
    print("\n\n\t\t\t*       *  *******  *       *******  ********  **     **  *******")
    print("\t\t\t*       *  *        *       *        *      *  * ** ** *  *		")
    print("\t\t\t*   *   *  *******  *       *        *      *  *   *   *  *******")
    print("\t\t\t*  ***  *  *        *       *        *      *  *       *  *       ")
    print("\t\t\t***   ***  *******  ******  *******  ********  *       *  *******  \n")
    print("\t\t  ****************************************************************************\n")
    
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
        print("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
        print("Good Afternoon Sir !")
  
    else:
        speak("Good Evening Sir !")
        print("Good Evening Sir !")
        
   
# call function
wishMe()



    
    
