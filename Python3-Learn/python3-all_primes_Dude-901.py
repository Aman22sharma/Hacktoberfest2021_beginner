# AUTHOR: Tanmay Khandelwal
# Python3 Concept: all primes upto n
# GITHUB: github.com/Dude-901

# Sieve Theorem

def sieve(p, n):
    for i in range(3, n+1, 2):
        p[i] = 1
    for i in range(3, n+1, 2):
        if p[i] == 1:
            for j in range(i*i, n+11, i):
                p[j] = 0

    p[2] = 1
    return p

for _ in range(int(input())):
    n = int(input())
    p = [0]*(n+1)
    p = sieve(p, n)
