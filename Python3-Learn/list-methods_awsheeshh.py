'''
AUTHOR: Ashish
Python3 Concept: List Manipulation and Methods in Python
GITHUB: https://github.com/awsheeshh
'''

# Let's take a list which we will use as an example.

my_list_1 = [2, 4, 5, 1] #This is a single data-type list.
my_list_2 = [2, "hello", 10, 13, 17, 13] #This is a mixed data-type list with both strings and integer in it.
my_list_3 = [3, [2, 1, 7], 9, 3] #This is a multi dimensional list.

#List Methods

#append() method
#appends the given element to the last index of the list.
'''
input: my_list_1.append(10)
       print(my_list_1)
output: [2, 4, 5, 1, 10]
'''

#insert() method
#Inserts the given element at given position of list.
'''
input: my_list_1.insert(0, 8) {0 is the index where you want to put element that is 8}
       print(my_list_1)
output: [8, 2, 4, 5, 1]
'''

#Accessing List Elements
#1. For Single Dimensional List
    '''
    input: print(my_list_1[0]) {0 is the index of the element you want to retrieve}
    output: 2
    '''
#2. For Multi Dimensional List
    '''
    my_list_3 = [3, [2, 1, 7], 9, 3] (list inside list)
    Suppose, we want to retrieve the 2nd element from the list which is inside my_list_3
    
    input: print(my_list_3[1][1]) {The second list is at index 1 of my_list_3 and we want to retreive 2nd element from it so we use [1] again}
    output: 1
    '''
  
#Removing Elements From List
#1. remove() method
    '''
    It removes the element specified from the list given that the element is present in the list.
    input: my_list_1.remove(2) -> will remove the first occurence of 2
           print(my_list_1)
    output: [4, 5, 1]
    '''
#2. pop() method
    '''
    It removes the last element of list by default but to remove an element at specific position you have to pass it's index value in function call.
    input1: my_list_1.pop() -> will remove last element
           print(my_list_1)
    output1: [2, 4, 5]
    
    input2: my_list_1.pop(0) -> will remove element at index 2.
            print(my_list_1)
    output2: [4, 5, 1]
    '''
  
#List Slicing
'''
input: print(my_list_1[1:]) -> will slice the list from index 1.
output: [4, 5, 1]

input: print(my_list_2[2:5]) -> will slice the list from index 2 upto index 4.
output: [10, 13, 17]

input: print(my_list_2[:-3]) -> will slice till 3rd element from the last
output: [2, "hello", 10]

>> list[::-1] reverses thee list but you can use list.reverse() method too.
'''

#sort() method
#Sorts the list in ascending or descending order.
'''
input: print(my_list_1.sort()) -> sorts in ascending order by default
output: [1, 2, 4, 5]

input: print(my_list_1.sort(reverse=True)) -> sorts in descending order
output: [5, 4, 2, 1]
'''

#Thanks for reading.
#Read python docs for more in depth understanding. 

