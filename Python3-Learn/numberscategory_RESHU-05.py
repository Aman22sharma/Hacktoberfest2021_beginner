print("*" * 50)
print(" " * 10,"Categories of Numbers")
print(" " *10," Check types of number")
print("*" * 50)
print("1. Palindrome\n\
2. Strong \n\
3. Armstrong \n\
4. Prime ")
n=int(input("Enter your choice"))
if n==1:
    n=int(input("Enter a Number"))
    p=n
    r=0
    while n!=0:
        d=n%10
        r=r*10+d
        n=n//10 
    if r==p:
        print(" It is a Palindrome Number")
    else:
        print("It is not a Palindrome Number")
elif n==2:
    n=int(input("Enter a Number"))
    p=n
    c=0
    while n!=0:
        d=n%10
        n=n//10
        f=1
        for x in range(1,d+1):
            f=f*x
        c=c+f
    if c==p:
        print("It is a Strong Number")
    else:
        print("It is not a strong number")
elif n==3:
    n=int(input("Enter a Number"))
    p=n
    c=0
    while n!=0:
        d=n%10
        n=n//10
        c=c+d**3
    if p==c:
        print("It is an Armstrong Number")
    else:
        print("It is not an  Armstrong Number")
elif n==4:
    n=int(input("Enter a Number"))
    for x in range(n):
        c=0
        for y in range(1,x+1):
            if x%y==0:
                c=c+1
    if c==2:
        print("It is a Prime Number")
    else:
        print("It is not a  Prime Number")
else:
    print("Invalid choice")
    
