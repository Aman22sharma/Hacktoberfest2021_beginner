# AUTHOR: Tanmay Khandelwal
# Python3 Concept: The Josephus problem, where 100 people standing in a circle, 1 kills 2 passes the sword to 3….who survives in the end?
# GITHUB: github.com/Tanmay-901

from sys import stdin,stdout                          

def Josephus_Prblm(n, k):
    if (n == 1): 
       return 1
    else: 
       return ((Josephus_Prblm(n - 1, k) + k-1) % n + 1)

for _ in range(int(stdin.readline())):
	N = int(stdin.readline())
  K = int(stdin.readline())
  print(Josephus_Prblm(N,K)

