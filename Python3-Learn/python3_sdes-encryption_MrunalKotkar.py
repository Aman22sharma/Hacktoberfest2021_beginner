# AUTHOR: Mrunal Kotkar
# Python3 Concept: simplified-des encryption algorithm implementation
# GITHUB: "https://github.com/MrunalKotkar"

# This is the cryptography algorith simplifies-des(data encryption standard) 
# implemented in Python language.
# example set of input - 
# 10 bit key - 1010000010
# 8 bit plaintext - 10010111
# output 
# 8 bit ciphertext - 00111000

#Tables required for respective permutations
P10table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8table = [6, 3, 7, 4, 8, 5, 10, 9]

IPtable = [2, 6, 3, 1, 4, 8, 5, 7]
EPtable = [4, 1, 2, 3, 2, 3, 4, 1]
P4table = [2, 4, 3, 1]
IPInvtable = [4, 1, 3, 5, 7, 2, 8, 6]

S0table = [[1,0,3,2], [3,2,1,0], [0,2,1,3], [3,1,3,2]]
S1table = [[0,1,2,3], [2,0,1,3], [3,0,1,0], [2,1,0,3]]

K1 = []
K2 = []

#permutation function
def perm(inputByte, permTable):
    outputList = []
    for i in range(len(permTable)):
        outputList.insert(i, inputByte[permTable[i]-1])
    return outputList

#function for left shift by 1 
def K1gen(outputList, permTable):
    x = int(len(permTable)/2)
    L1 = outputList[:x]
    L2 = outputList[x:]
    L1.append(L1.pop(0))
    L2.append(L2.pop(0))
    K1 = L1+L2
    return K1

#function for left shift by 2
def K2gen(outputList, permTable):
    x = int(len(permTable)/2)
    L1 = outputList[:x]
    L2 = outputList[x:]
    L1.append(L1.pop(0))
    L1.append(L1.pop(0))
    L2.append(L2.pop(0))
    L2.append(L2.pop(0))
    K2 = L1+L2
    return K2

#Function for Expanding 4bits to 8bits
def Expandbits(OutputList, EPTable):
    EPList = []
    for i in range(len(EPTable)):
        EPList.insert(i, OutputList[EPTable[i]-1])
    return EPList

#Function for generation of S 
def Sboxes(HalfList, matrix):
    a = int(str(HalfList[0]) + str(HalfList[3]), 2)
    b = int(str(HalfList[1]) + str(HalfList[2]), 2)
    S = bin(matrix[a][b]).replace('0b','')
    return S

def generateSbox(l1, l2):
    S0 = Sboxes(l1, S0table)
    S1 = Sboxes(l2, S1table)
    S = str(S0)+str(S1)
    S = [int(x) for x in str(S)]
    return S

def fk(IP8, key):
    #convert it into 2 halves
    x = int(len(IP8)/2)
    L = IP8[:x]
    R = IP8[x:]
    #expand right 4 bits of IP output
    Op1 = Expandbits(R, EPtable)
    #XOR EP output with K1
    XOR1 = list(a^b for a,b in zip(Op1,key))
    #divide it into two halves
    Lhalf = XOR1[:4]
    Rhalf = XOR1[4:]
    #Generate s box from these two halves
    S1 = generateSbox(Lhalf, Rhalf)
    #Apply P4 permutation on the answer
    P41 = perm(S1, P4table)
    #XOR of left part of IP8 and P4 permutate
    XOR2 = list(a^b for a,b in zip(L,P41))
    #Combining this result with right half of IP
    C = XOR2 + R
    return C
    
def printlist(list):
    st = ''.join([str(elem) for elem in list])
    return st

def Keygen(Key):
    key = [int(x) for x in str(Key)]
    IP10 = perm(key, P10table)   #P10 permutation on key
    K11 = K1gen(IP10, P10table)  #shifting operation on the output of P10 of key
    K1 = perm(K11, P8table)      #8 bit permutation on key
    K21 = K2gen(K11, P10table)   #double shift operation on the output of P10 of key
    K2 = perm(K21, P8table)      #8 bit permutation on key
    return K1, K2

def encrypt(plainText, K1, K2):
    plainText = [int(x) for x in str(plainText)]
    IP8 = perm(plainText, IPtable)       #Inittial permutation on plaintext
    print("IP Output: " + printlist(IP8))
    Mid1 = fk(IP8, K1)
    print("first Fk output: " + printlist(Mid1))
    #Swap left and right part
    swap = []
    swap += Mid1[4:]
    swap += Mid1[:4]
    #Round 2 of Fk starts from here
    Mid2 = fk(swap, K2)
    print("Second Fk output: " + printlist(Mid2))
    #Apply IP inverse 
    CipherText = perm(Mid2, IPInvtable)
    return CipherText


key = input("Enter 10 bit binary key: ")
plainText = input("Enter 8 bit plaintext: ")

K1, K2 = Keygen(key)
print("\nGenerated keys are: ")
print("K1: " + printlist(K1))
print("K2: " + printlist(K2))
CipherText = encrypt(plainText, K1, K2)
print("Generated CipherText: " + printlist(CipherText))





