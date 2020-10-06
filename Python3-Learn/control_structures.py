# AUTHOR: InfernapeXavier
# Python3 Concept: Python Control Structures
# GITHUB: https://github.com/InfernapeXavier


#Change the number and check the outputs
number = 5 

# If-Else
if number <= 5:
    print ("Less than or equal to 5")
else:
    print ("Greater than 5")
  

# If-Elif-Else
if number < 5:
    print ("Less than 5")
elif number == 5:
    print ("Equal to 5")
else:
    print ("Greater than 5")

# For Loop

# Variant 1: When you have a range

for i in range(0, 5):
    print (i, end="")
print()

for i in range(0,5,2): #Step value of 2
    print (i, end="")
print()

for i in range(5, 0, -1): #Negative step value
    print (i, end="")
print()

# Variant 2: When you have a data structure to iterate through
nums = [1,2,3,4,5,6,7,8]

for num in nums:
    print (num, end="")
print()

# Variant 3: For-Else - The else block is executed when the for loop isn't entered

for i in range(1, 5):
    print (i, end="")
else:
    print ("\nExited the for loop")


# While Loop

i = 5

while i > 0:
    print (i, end="")
    i -= 1
else:
    print ("\nExited while loop")