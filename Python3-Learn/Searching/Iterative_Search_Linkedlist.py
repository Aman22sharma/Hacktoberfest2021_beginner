# Iterative Python program to search an element in linked list
 
# Node class
class Node:
     
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data 
        self.next = None
 
# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None 
 
    # This function insert a new node at the beginning of the linked list
    def add_node(self, new_data):
     
        # Create a new Node
        new_node = Node(new_data)
 
        # Make next of new Node as head
        new_node.next = self.head
 
        # Move the head to point to new Node
        self.head = new_node
 
    # This Function checks whether the value ele present in the linked list
    def search(self, ele):
 
        # Initialize current to head
        current = self.head
 
        # loop till current not equal to None
        while current != None:
            if current.data == ele:
                return True # ele found
             
            current = current.next
         
        return False # ele Not found
 
 
# Driver Code to test the algorithm
if __name__ == '__main__':
 
    llst = LinkedList()
 
    llst.add_node(10);
    llst.add_node(20);
    llst.add_node(31);
    llst.add_node(21);
 
    if llst.search(20):
        print("Yes")
    else:
        print("No")
