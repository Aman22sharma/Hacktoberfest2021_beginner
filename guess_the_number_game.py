# Author: Sanchit Sharma

import random
logo = """
__________.__               ________                         _____ .____    .__  _____       
\__    ___|  |__   ____    /  _____/_____    _____   ____   /  |  ||    |   |___/ ____\____  
  |    |  |  |  \_/ __ \  /   \  ___\__  \  /     \_/ __ \ /   |  ||    |   |  \   ___/ __ \ 
  |    |  |   Y  \  ___/  \    \_\  \/ __ \|  Y Y  \  ___//    ^   |    |___|  ||  | \  ___/ 
  |____|  |___|  /\___  >  \______  (____  |__|_|  /\___  \____   ||_______ |__||__|  \___  >
               \/     \/          \/     \/      \/     \/     |__|        \/             \/ 

"""

chosenNumber = random.randrange(1, 100)
difficulty = input("Choose a difficulty. 'easy' or 'hard': ")

if difficulty == 'easy':
    chances = 10
else :
    chances = 5

def game(chances):
    print(logo)
    while chances > 0:
        print(f"Chances left are {chances}")
        opt = int(input("Enter your guessed number bw 1 to 100: "))
        if opt == chosenNumber:
            print("You won.👍")
            break
        if opt > chosenNumber:
            print("Your guess is too high. 🤦‍♂️")
        elif opt < chosenNumber:
            print("Your guess is too low. 🤦‍♀️")
        chances -= 1
    print(f"The correct answer was {chosenNumber}. You fool. 🤷‍♂️")

game(chances)
