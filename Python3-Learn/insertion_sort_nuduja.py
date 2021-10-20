#Creating an Empty List
arr=[]


#Ask the number of input from the user to
n = int(input("Enter the number of Elements"))

print("Enter the Numbers: ")
for i in range(0,n):
    ele = int(input())
    arr.append(ele) #Adding set of elements to the array/list

print(arr)

#Function to do the Insertion Sort

def insertionSort(arr):
    #Traverse through 1 to len(arr)

    for i in range(1, len(arr)):
        key=arr[i]
        #Move elements of arr[0..i-1], that are
        #greater than key, to one position ahead of key
        #of their current position

        j = i - 1

        while (j >= 0 and key < arr[j]):
            arr[j+1]=arr[j]
            j= j - 1
        arr[j+1]=key

#Calling the function
insertionSort(arr)

#printing the sorter array
print("Sorted Array is: ")

#for i in range (len(lst)):
# print("%d" %lst[i])
print(arr)