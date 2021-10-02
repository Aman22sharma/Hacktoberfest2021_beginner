# AUTHOR: Priyanshu Pathak
# Python3 Concept: Data-Structure -- > Stack
# GITHUB: https://github.com/priyanshu-28

#Add your python3 concept below
#Stack
#A stack is a linear data structure
 
#Access limited to a last-in first-out order.
 
#Adding and removing items is restricted to one end known as the top of the stack.
 
#An empty stack contains no items.

#Operations: 
#Stack() --> Creates a new empty stack.
#isEmpty() --> Returns a boolean value indicating if the stack is empty.
#length() --> Returns the number of items in the stack.
#pop() --> Removes and returns the top item of the stack
#peek() --> Returns a reference to the item on top of a non-empty stack without removing it.
#push(item) --> Adds the given item to the top of the stack.

# Implementation of the Stack ADT using a Python list.
class Stack :

    # Creates an empty stack.
    def __init__( self ): 
        self._theItems = list()

    # Returns True if the stack is empty or False otherwise.
    def isEmpty( self ): 
        return len( self ) == 0

    # Returns the number of items in the stack.
    def __len__ ( self ):
        return len( self._theItems )

    # Returns the top item on the stack without removing it.
    def peek( self ):
        assert not self.isEmpty(), "Cannot peek at an empty stack" 
        return self._theItems[-1]

    # Removes and returns the top item on the stack.
    def pop( self ):
        assert not self.isEmpty(), "Cannot pop from an empty stack" 
        return self._theItems.pop()

    # Push an item onto the top of the stack.
    def push( self, item ): 
        self._theItems.append( item )
