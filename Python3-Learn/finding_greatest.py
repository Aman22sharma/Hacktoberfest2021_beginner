# AUTHOR: Ankur
# Python3 Concept: Finding greatest no amongst the following
# GITHUB: https://github.com/ankur12-1610

#Add your python3 concept below


num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
