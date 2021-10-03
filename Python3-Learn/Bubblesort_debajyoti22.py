"""
AUTHOR: Debajyoti Das
Python3 Concept: Bubble Sorting in Python
GITHUB: https://github.com/debajyoti22

Bubble Sort is a simple sorting algorithm that works iteratively by checking and swapping the adjacent elements if they are present in the wrong order.
"""

def bubble(a):
    n = len(a)    
    for i in range(n):
        for j in range(0,n-1):
            if(a[j]>a[j+1]):
                tmp = a[j]
                a[j]= a[j+1]
                a[j+1] = tmp                
    for i in range(n):
        print(a[i],end=" ")
       
     
                
                
a = input().split()
bubble(a)
            
