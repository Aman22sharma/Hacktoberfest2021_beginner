# Python program to find the factorial of a number using recursion
 def factorial(n: int):
    return n * factorial(n - 1) if n > 1 else 1

