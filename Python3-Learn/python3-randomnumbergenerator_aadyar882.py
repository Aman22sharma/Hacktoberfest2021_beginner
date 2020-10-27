"""
// AUTHOR: Aadya Rangole
// Python3 Concept: Random Number Generator (generates a list of random numbers given a list length and a minimum value)
// GITHUB: github.com/aadyar882

//Add your python3 concept below
"""
import random
lis = []
def randnumbergenerator():
    range_n = input("How many numbers do you want to generate?: ")
    minval = input("What is the minimum value you want to generate?: ")
    while len(lis) <= 10: 
        lis.append(int(range_n)*random.random()+int(minval))
        if len(lis) == 10 :
            break
    print(lis)
