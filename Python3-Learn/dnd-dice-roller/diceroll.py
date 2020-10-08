import random

def diceroll():
    sides = input("What die type: ")
    quantity = input("How many: ")
    total = 0
    if sides == "d4":
        die = 4
    elif sides == "d6":
        die = 6
    elif sides == "d10":
        die = 10
    elif sides == "d12":
        die = 12
    elif sides == "d20":
        die = 20
    elif sides == "d100":
        die = 100
    else:
        print("That is not a die type")

    for i in quantity:
        result = (random.randint(1, die))
        print(i, sides, " = ", result)
        total = total + result
    return total
