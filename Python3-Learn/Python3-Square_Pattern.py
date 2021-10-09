'''Name : Rohan Rajeev Bharadwaj
Python3 Concept : Loops
Github Profile Link : https://github.com/Rohanrbharadwaj'''

def print_square(n):
  for i in range(1, n+1):
      for j in range(1, n+1):
          if i == 1 or j==1 or i == n or j == n:
              print('*', end = '')
          else:
              print(' ', end = '')
      print()
    
