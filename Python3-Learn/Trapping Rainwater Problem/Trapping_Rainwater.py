def water_trapped(arr,n):
    result=0
    for i in range(1,n-1):
        l=int(arr[i])
        for j in range(0,i):
            l=max(l,int(arr[j]))
        r=int(arr[i])
        for k in range(i+1,n):
            r=max(r,int(arr[k]))

        x=min(l,r)
        result+=x-int(arr[i])

    return result

n=int(input("Enter the length of the array : "))
print("")
print("Enter each element of the array by giving a ',' after each element : ")
element=input()
element=element.split(",")
result=water_trapped(element,n)
print("")
print("The water trapped is : ",result," units")