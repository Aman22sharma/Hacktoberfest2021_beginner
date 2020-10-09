"""
// AUTHOR: Russ Carroll
// Python3 Concept: Take die type and quantity arguments from user and then simulate those dice rolls and providing the results
// GITHUB: your github profile link

//Add your python3 concept below

The purpose of this program is to roll a quantity number of die type dice and provide the user with the results"""
import random

die = input("What die type (default is d6): ") or "d6"
quantity = input("How many (default is 1): ") or 1
quantity = int(quantity)
total = 0

#There is probably a more eliegant way to do this but I don't know how
if die == "d4":
   sides = 4
elif die == "d6":
   sides = 6
elif die == "d10":
   sides = 10
elif die == "d12":
   sides = 12
elif die == "d20":
   sides = 20
elif die == "d100":
   sides = 100
else:
   print("That is not a die type")

for i in range(0, quantity):
   result = (random.randint(1, sides))
   print(i+1, die, " = ", result)
   total += result
print("This is the result of your roll: ", total)
