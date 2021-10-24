// AUTHOR: Vishnu Ram V
// Python3 Concept: Fibonacci sequence
// GITHUB: github.com/vishnuramv

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
         
         
def fib():
     n = int(input())
     a = 0
     b = 1
     p = []
     for i in range(n):
         p.append(a)
         a,b = b,a+b
     print(p)
fib()
