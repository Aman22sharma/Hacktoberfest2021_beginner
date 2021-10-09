# AUTHOR: Max Müller
# Python3 Concept: Heap Sort Algorithm
# GITHUB: https://github.com/MMVonnSeek

# heapify tree rooted at index i

def heapify(arr, n, i): 
    largest = i       # In max-heap largest is at root 
    l = 2 * i + 1     # left child index = 2*i + 1 
    r = 2 * i + 2     # right child index = 2*i + 2 
  
    # See if left child of root exists and > root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and > root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # update root if required 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root 
        heapify(arr, n, largest) 
  
  
# heap sort definition
def heapSort(arr): 
    n = len(arr) 
  
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # extracting elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 
  
 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i])
    