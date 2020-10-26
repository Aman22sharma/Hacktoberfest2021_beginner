#  9.	Write a Python program to get a string which is n (non-negative integer) copies of a given string

str = input('Enter any String value:   ')
num = int(input('Enter the number of copies you want of the string:  '))
final = ''
for i in range(num):
    final = final + str

print(final)
