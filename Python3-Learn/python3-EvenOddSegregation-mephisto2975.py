# AUTHOR: Parth Kholkute
# Python3 Concept: Array Rotation
# GITHUB: github.com/mephisto2975
 
def segregateEvenOdd(arr):
 
    # Initialize left and right indexes
    left = 0
    right = len(arr)-1

    while left < right:
 
        # Increment left index while we see 0 at left
        while (arr[left]%2==0 and left < right):
            left += 1
 
        # Decrement right index while we see 1 at right
        while (arr[right]%2 == 1 and left < right):
            right -= 1
 
        if (left < right):
              # Swap left element of arr with right element
              arr[left],arr[right] = arr[right],arr[left]
              left += 1
              right = right-1
 
 #Driver function
arr = [29, 7, 98, 9, 30, 2, 74, 67]
segregateEvenOdd(arr)
print ("Array after segregation "),
for i in range(0,len(arr)):
    print (arr[i], end=" ")