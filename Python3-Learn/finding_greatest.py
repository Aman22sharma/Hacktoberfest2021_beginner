# AUTHOR: Ankur
# Python3 Concept: Finding greatest no amongst the following
# GITHUB: https://github.com/ankur12-1610

#Add your python3 concept below


num1 = Input("Enter First Number: ")
num2 = Input("Enter Second Number: ")
num3 = Input("Enter Third Number: ")

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
