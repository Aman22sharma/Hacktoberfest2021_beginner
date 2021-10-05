# AUTHOR : Adwait Patil
# Linked List in Python
# https://github.com/adwait41001/

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        tmp = self.head
        if (tmp):
            while(tmp.next):
                print(tmp.data,end='->')
                tmp = tmp.next
            print(tmp.data)
        else:
            print("The list is empty")
    def pushBack(self,data):
        tmp = self.head
        if tmp:
            while(tmp.next):
                tmp = tmp.next
            tmp.next = Node(data)
        else:
            self.head = Node(data)
    def pushFront(self,data):
        tmp = self.head
        if tmp:
            tmp2 = Node(data)
            tmp2.next = tmp
            self.head = tmp2
        else:
            self.head = Node(data)
            
    def topFront(self):
        tmp = self.head
        if tmp:
            return tmp.data
        else:
            return "Empty List"
            
    def popFront(self):
        tmp = self.head
        if tmp:
            if tmp.next:
                self.head = tmp.next
                del tmp
            else:
                self.head = None
                del tmp
    def popBack(self):
        tmp = self.head
        if tmp:
            if tmp.next:
                while(tmp.next.next):
                    tmp = tmp.next
                tmp.next = None
            else:
                self.head = None
        else:
            print("Empty List")
            
    def find(self,key):
        tmp = self.head 
        if tmp:
            while(tmp):
                if tmp.data == key :
                    return True
                tmp = tmp.next
        return False
    def erase(self,key):
        count = 0 
        tmp = self.head
        if tmp:
            if tmp.data == key:
                count = 1
                if tmp.next:
                    self.head = tmp.next
                else:
                    self.head = None
            while(tmp):
                if tmp.next:
                    if tmp.next.data == key:
                        count = 1
                        if tmp.next.next:
                            tmp.next = tmp.next.next
                        else:
                            tmp.next = None
                    tmp = tmp.next
                else:
                    break
            if count == 0:
                print("Element not found")
        else:
            print("Empty List")
    
    def empty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def addBefore(self,node,key):
        tmp = self.head
        if tmp:
            if tmp == node:
                pushFront(key)
            else:
                while(tmp):
                    if tmp.next == node :
                        tmp2 = Node(key)
                        tmp2.next = tmp.next
                        tmp.next = tmp2
                    tmp = tmp.next
        else:
            self.head = Node(key)
    def addAfter(self,node,key):
        tmp = self.head
        if tmp:
            if tmp == node:
                pushBack(key)
            else:
                while(tmp):
                    if tmp == node :
                        tmp2 = Node(key)
                        tmp2.next = tmp.next
                        tmp.next = tmp2
                    tmp = tmp.next
        else:
            self.head = Node(key)
            
def convertArrayToLinkedList(arr):
    arrLL = LinkedList()
    for i in arr:
        arrLL.pushBack(i)
    return arrLL