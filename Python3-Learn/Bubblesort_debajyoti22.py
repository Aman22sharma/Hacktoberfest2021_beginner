def bubble(a):
    n = len(a)
    c = 0
    for i in range(n):
        for j in range(0,n-1):
            if(a[j]>a[j+1]):
                tmp = a[j]
                a[j]= a[j+1]
                a[j+1] = tmp
                c = c + 1
    for i in range(n):
        print(a[i],end=" ")
       
     
                
                
a = input().split()
bubble(a)
            
