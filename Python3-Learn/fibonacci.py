def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
a= int(input("Enter a number-"))
if a < 0:
    print("Incorrect input")
else:
    for i in range(a):
        print(Fibonacci(i),end=" ")
