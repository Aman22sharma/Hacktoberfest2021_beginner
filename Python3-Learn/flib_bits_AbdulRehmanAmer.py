'''
AUTHOR: Abdul Rehman Amer
Python3 Concept: Flip 8 bits using bit wise operation
GITHUB: https://github.com/AbdulRehmanAmer

Here we are flipping the bits of n and printing the number formed by flipping bits
'''
def flip_Bits(n):
    for i in range(8): #8 bits
        if n & (2**i) == 0:
            n = n | (2 ** i)
        else:
            n = n & (((2**8)-1) - (2**i)) #flipping ith bit to 0
    return n

if __name__ == "__main__":
    n = int(input())
    print(flip_Bits(n))

