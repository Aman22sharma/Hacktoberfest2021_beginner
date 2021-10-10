# AUTHOR: Aaditya Kumra
# Python3 Concept:String,patterns
# GITHUB: https://github.com/AadityaKumra


#Pattern size must be N X M. (N is an odd natural number,M and is 3 times N.)
#Size constraints to ensure proper pattern implementation.
#input example= 5 15 ,10 30 
t=input("Enter Dimension of pattern(a b):") 
s=list(map(int,(t.split(" "))))
a=s[0]
b=s[1]
z=list()
for i in range(0,a):
    if i%2!=0:
        z.append(i)
e=int((a-1)/2)
c=int(b)    
for i in range(0,e):
    print("-"*int((c-3)/2)+".|."*int(z[i])+"-"*int((c-3)/2))
    c-=6
print("-"*int((b-7)/2)+"WELCOME"+"-"*int((b-7)/2))

for i in range(e-1,-1,-1):
    print("-"*int((c+3)/2)+".|."*int(z[i])+"-"*int((c+3)/2))
    c+=6
