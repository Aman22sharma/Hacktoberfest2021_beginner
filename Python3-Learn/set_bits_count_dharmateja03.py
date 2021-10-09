# AUTHOR: Dharma Teja
# Python3 Concept:counting number of set bits in a number
# GITHUB: https://github.com/dharmateja03
nunber=int(input())  #enter input
result=0 
while number:
  if number % 2 == 1:
      result += 1
  number = number >> 1
print(result)

