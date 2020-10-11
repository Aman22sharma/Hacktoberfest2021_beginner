
"""
// AUTHOR: Sanjay Kumar
// Python3 Concept: Binary Search Algorithm
// GITHUB: https://github.com/iamsnj
"""

def binary_search(arr, key):
    """
    Function to find index of an element
    in a sorted array with binray search algorithm.
    If element is found then it returns index of element in array
    else, return -1
    """

    """
    Input: Input is in two lines
        array of integers (first line)
        key (second line)
    Output: key (element to be searched in the array)

    Example:
    Input0: [1, 2, 3, 4, 5, 6]
           5
    Output0: 4

    Input1: [1, 2, 3, 4, 5, 6]
            9
    Output1: -1

    """

    n = len(arr) # size of array
    low, high = 0, n-1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == key: # we found the key
            return mid
        if arr[mid] < key:
            low = mid+1
        else:
            high = mid-1
        
    return -1
    
arr = [1, 2, 3, 4, 5, 6]
key = 3
print(binary_search(arr, key))
