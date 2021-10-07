// AUTHOR: Avyay Jain
// Python3 Concept: (calculator)
// GITHUB: https://github.com/avyayjain
        
import random 

level = int(input("\n enter the level (1- Easy,2-Medium,3-Hard)"))

if(level == 1):
    for i in range (0,3):
        a= random.randint(0,10)
        guess = int(input("\nEnter the no"))
        if(guess<a):
            print("\nmore")
        elif(guess>a):
             print("\n less")
        elif(guess==a):
             print("\nWIn")    
        i+=1        
elif(level == 2):
    for y in range (0,3):
        a= random.randint(0,20)
        guess = int(input("\nEnter the no"))
        if(guess<a):
            print("\n more")
        elif(guess>a):
             print("\n less")
        elif(guess==a):
             print("\n WIn")
    y+=1
elif(level == 3):
    for k in range (0,3):
        a= random.randint(0,30)
        guess = int(input("\n Enter the no"))
        if(guess<a):
            print("\n more")
        elif(guess>a):
             print("\n less")
        elif(guess==a): print("\n WIn")
    k+=1
else: quit()
