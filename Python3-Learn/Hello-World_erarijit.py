// AUTHOR: Arijit Mukherjee
//Python3 Concept: Hello World Program
// GITHUB: https://github.com/erarijit

print("Hello World! Welcome to Github")
print("well come to the calculator")
import numpy as np
a='addition'
s='subraction'
m='multiplication'
d='division'
calc=input('yo want addition(a), Subtraction(s), Multiplication(m), or division(d)?')
if calc =='a':
    num1=float(input(''))
    num2=float(input(''))
    print(num1+num2)
elif calc== 's':
    num1=float(input(''))
    num2=float(input(''))
    print(num1-num2)
elif calc=='m':
    num1=float(input(''))
    num2=float(input(''))
    print(num1*num2)
elif calc=='d':
    num1=float(input(''))
    num2=float(input(''))
    print(num1/num2)
else:
    print('Please use the letters in paranthesis to indicate the operation')
