#AUTHOR:  Ankita Mandal 
#Python3 Concept: Python Lambda
#GITHUB: https://github.com/GoGi2712

from itertools import *

# Easy joining of two lists into a list of tuples
for i in izip([1, 2, 3], ['a', 'b', 'c']):
    print i
# ('a', 1)
# ('b', 2)
# ('c', 3)

# The count() function returns an interator that 
# produces consecutive integers, forever. This 
# one is great for adding indices next to your list 
# elements for readability and convenience
for i in izip(count(1), ['Bob', 'Emily', 'Joe']):
    print i
# (1, 'Bob')
# (2, 'Emily')
# (3, 'Joe')    

# The dropwhile() function returns an iterator that returns 
# all the elements of the input which come after a certain 
# condition becomes false for the first time. 
def check_for_drop(x):
    print 'Checking: ', x
    return (x > 5)

for i in dropwhile(should_drop, [2, 4, 6, 8, 10, 12]):
    print 'Result: ', i

# Checking: 2
# Checking: 4
# Result: 6
# Result: 8
# Result: 10
# Result: 12


# The groupby() function is great for retrieving bunches
# of iterator elements which are the same or have similar 
# properties

a = sorted([1, 2, 1, 3, 2, 1, 2, 3, 4, 5])
for key, value in groupby(a):
    print(key, value), end=' ')
    
# (1, [1, 1, 1])
# (2, [2, 2, 2]) 
# (3, [3, 3]) 
# (4, [4]) 
# (5, [5]) 