# Python3-Learn

//  AUTHOR: Sumit Sah
//  Python3 Concept: Check Magic number 
//  GITHUB: https://github.com/sumitbro

# Magic number concept
#A magic number is that number whose repeated sum of its digits till we get a single digit is equal to 1.

# Example:

# original number= 1729
# sum of digits= 1+7+2+9=19
#                1+9=10
#                1+0=1
# 1729 is magic number

#code

import math

num = int(input("Enter a Number \n"))
digitCount = int(math.log10(num))+1
sumOfDigits = 0

temp = num #copying num

#calculating sum of digits of temp(i.e num) until
#sumOfDigits is a single digit
while( digitCount > 1):

  sumOfDigits = 0

  while(temp > 0):
    sumOfDigits += temp%10
    temp = temp//10

  temp = sumOfDigits
  #count the digits of sumOfDigits
  digitCount = int(math.log10(sumOfDigits))+1
   
    
#check whether sumOfDigits == 1
if(sumOfDigits == 1):
    print("Magic number")
else:
    print("Not a magic number")