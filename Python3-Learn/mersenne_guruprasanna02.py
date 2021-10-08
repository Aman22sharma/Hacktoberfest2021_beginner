# // AUTHOR: Guruprasanna
# // Python3 Concept: Mersenne numbers/functions
# // GITHUB: https://github.com/Guruprasanna02

# // Add your python3 concept below
# To print first "n" mersenne numbers

def mersenne(n):
    for i in range(2,n+2):
        print((2**i) - 1,end="\n") 

n = int(input("Enter an integer : "))
mersenne(n)