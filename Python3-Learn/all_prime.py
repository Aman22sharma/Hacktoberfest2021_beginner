# Sieve Theorem
from math import *

def primes(n):
    pr = [True] * (n+1)
    pr[0] = False
    pr[1] = False
    for x in range(2, int(sqrt(n))+1):
        if pr[x] == True:
            for i in range(x*x,n+1,x):
                pr[i] = False
    for i in range(len(pr)):
        if pr[i] == True:
            print(i, end=" ")

for _ in range(int(input())):
    n = int(input())
    primes(n)