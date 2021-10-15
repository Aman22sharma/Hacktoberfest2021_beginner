# Created By Tanmay Pandey - Beginner Hacktober fest 2021

print("Welcome to computer quiz!")

score = 0

qs = [
    "How many bits are present in a byte?",
    "Google is a Browser or a Search Engine?",
    "Who is the founder of Facebook?",
    "Who invented the first computer?",
    "What does PSU stand for?",
    "Full form of VIRUS is?",
    "What is the address given to a computer connected to a network called?"
    ]  
    
ans = ['8',
       "Search Engine",
       "Mark Zuckerberg",
       "Charles Babbage",
       "Virtual Information Resource Under Seize",
       "power supply",
       "IP address"
      ]

i=0
while(i<7):
    i = i+1
    question = qs[i-1]
    answer = input(question)
    if answer.lower() == ans[i-1].lower():
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / len(qs)) * 100) + "%.")
    