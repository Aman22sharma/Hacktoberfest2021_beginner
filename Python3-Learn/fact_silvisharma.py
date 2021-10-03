class Factorial:
    def fact(self,n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f

n = int(input("Enter a number:"))

obj=Factorial()
f=obj.fact(n)
print("The factorial of",n,"is",f)
