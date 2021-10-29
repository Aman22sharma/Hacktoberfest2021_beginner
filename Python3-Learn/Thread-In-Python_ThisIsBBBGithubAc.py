# AUTHOR: Bidyut Bikash Bharali
# Python3 Concept: Thread-In-Python
# GITHUB: https://github.com/ThisIsBBBGithubAc

from threading import Thread
from time import sleep

def print_something(line):
    while True:
        print("Hello this is running on thread\n")
        print(line, "\n\n\n")
        sleep(3)


if __name__ == '__main__':
    t0 = Thread(target=print_something, args=("I'm using Python3",), daemon = True)
    t0.start()
    
    t1 = Thread(target=print_something, args=("I'm using Python3",))
    t1.start()
    