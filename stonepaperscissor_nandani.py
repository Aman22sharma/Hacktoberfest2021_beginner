// this is stone paper scissor game in python
import random 

print("STONE PAPER SCISSOR GAME")

print('''        s for Stone 
        p for paper
        x for scissor ''')

lt = ["s","p","x"]
u_score = 0
bot_score = 0
tot_chances = 10
no_of_choices = 0

while(no_of_choices < tot_chances):

    user = input("Enter your choice :")
    bot = random.choice(lt) 

    print(f"\nyou chose {user} , computer chose {bot} \n")

    if user == bot :
        print(f"Both player selected {user} , it's a tie..")
        print(f"Scores : user = {u_score} computer ={bot_score}")
    elif user == 's':
        if bot == 'p':
            bot_score += 1
            print("Paper covers stone! You lose")
            print(f"Scores : user = {u_score} computer ={bot_score}")

        else:
            u_score += 1
            print("Stone smashes scissors! You win")
            print(f"Scores : user = {u_score} computer ={bot_score}")

    elif user == 'p':
        if bot == 's':
            u_score += 1
            print("Paper covers stone! You win")
            print(f"Scores : user = {u_score} computer ={bot_score}") 
        else:
            bot_score += 1
            print("Scissor cuts paper! You lose")
            print(f"Scores : user = {u_score} computer ={bot_score}")

    elif user == 'x':
        if bot == 'p':
            u_score += 1
            print("Scissor cuts paper! You win")
            print(f"Scores : user = {u_score} computer ={bot_score}") 
        else:
            bot_score += 1
            print("Stone smashes scissor! You lose")
            print(f"Scores : user = {u_score} computer ={bot_score}")

    no_of_choices +=1

    print("press c for continue | press q for exit")
    choice = ""
    while(choice != "c" and choice != "q"):
        choice = input()
        if choice == "q":
            exit()
        elif choice == "c":
            continue
