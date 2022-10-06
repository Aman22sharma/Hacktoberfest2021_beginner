##QUESTION17
##Binary Search Technique


def Bsearch(key,lst):
    low=0
    high=len(lst)-1
    while low<=high: 
        mid=(high+low)//2  # Getting middle value in array 
        if lst[mid]==key:
            return mid
        elif key<lst[mid]: # if key<middle element means higher index needs
            #to be modified as right side wasted 
            high=mid-1
        else: #if key>middle element means left side waste and lower index needs
            #to be  modified as mid+1
            low=mid+1
    else:
        return -1
l=[]
n=int(input('Enter how many items:'))
for i  in range(n):
    a=int(input('Enter integer: '))
    l.append(a)
key=int(input("Enter value to be search in array :"))
print(l)
a=Bsearch(key,l)
if a==-1:
    print("Element not foiund in array")
else:
    print(f'Element found at position {a+1}')

































    
