'''Python Program to check if a number is prime or not 

What is a prime number?
A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
2, 3, 5, 7 etc. are prime numbers as they do not have any other factors
'''


num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
      print(num, "is a prime number")   
else:
    print(num, "is not a prime number")

'''
Input: 5
Output: 5 is a prime number
Input:10
Output:10 is not a prime number

'''
