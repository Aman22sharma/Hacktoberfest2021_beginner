'''Name : Rohan Rajeev Bharadwaj
Python3 Concept : Loops
Github Profile Link : https://github.com/Rohanrbharadwaj'''

def print_x(n):
  for i in range(1, n+1):
      for j in range(1, n+1):
          if i == j or i+j == n+1:
              print('*', end = '')
          else:
              print(' ', end = '')
      print()
    
