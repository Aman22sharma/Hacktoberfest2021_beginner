"""
Name : Simple Interest Calculator
Author : [Mayank Goyal) [https://github.com/mayankgoyal-13]
"""

print('Welcome, to simple interest calculator')
principal = int(input('Enter your principal amount: '))
roi = float(input('Enter your rate of interest: '))
time = float(input('Enter the time period/tenure in yrs: '))
simple_interest = (principal*roi*time)/100
print('Your simple interest at the end of ' + str(time) + 'years will be: ' + str(simple_interest))
