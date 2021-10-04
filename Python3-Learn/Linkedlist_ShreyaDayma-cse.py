//Author: Shreya Dayma
//Python3 concept: Linked list insertion, deletion and length of nodes.
//Github: https://github.com/ShreyaDayma-cse

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        n = Node(data,self.head)
        self.head = n
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,self.head)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data,None)    
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            itr = self.head
            l=' '
            while itr is not None:
                l+= str(itr.data) + '-->'
                itr = itr.next
            print(l)
    
    def get_length(self):
        c=0
        itr = self.head
        while itr:
            c+=1
            itr=itr.next
        return c
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            print("Invalid Index")
        elif index==0:
            self.head = self.head.next
            return
        else:
            c=0
            itr=self.head 
            while itr:
                if c==index-1:
                    itr.next=itr.next.next
                    break
                itr=itr.next
                c+=1
                
if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(7)
    ll.insert_at_end(8)
    ll.insert_at_end(2)
    print(ll.get_length())
    ll.print()
    ll.remove_at(3)
    ll.print()
