from SinglyLL import linkedList
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Circularll:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def print_list(self):
        curr = self.head
        if curr is None:
            return
        while curr.next != self.head:
            print(curr.data)
            curr = curr.next
        print(curr.data)

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node

    def remove(self, key):
        cur = self.head
        prev = None
        if cur and cur.data == key:
            self.head = cur.next
            self.tail.next = self.head
            cur = None
            return
        elif self.tail.data == key:
            while cur.next.next != self.head:
                cur = cur.next
            self.tail = cur
            self.tail.next = self.head
            cur = None
            return
        else:
            while cur and cur.data != key:
                prev = cur
                cur = cur.next
            prev.next = cur.next
            cur = None
            return

    def remove_node(self, node):
        cur = self.head
        prev = None
        if cur == node:
            self.head = cur.next
            self.tail.next = self.head
            cur = None
            return
        elif self.tail == node:
            while cur.next.next != self.head:
                cur = cur.next
            self.tail = cur
            self.tail.next = self.head
            cur = None
            return
        else:
            while cur != node:
                prev = cur
                cur = cur.next
            prev.next = cur.next
            cur = None
            return

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count+= 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head
        count = 0
        mid = size//2
        splitted_ll = Circularll()
        cur = self.head
        prev = None
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        while cur != self.head:
            splitted_ll.append(cur.data)
            cur = cur.next

        self.tail = prev
        self.print_list()
        print("\n")
        splitted_ll.print_list()

    def josephus_problem(self, step):
        cur = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            self.remove_node(cur)
            cur = cur.next

    def is_circular_llist(self, input_list):
        cur = input_list.head
        while cur:
            cur = cur.next
            if cur == input_list.head:
                return True
        return False

ls1 = Circularll()
ls1.append(1)
ls1.append(2)
ls1.append(3)
ls1.append(4)
ls1.append(5)
ls1.append(6)
ls1.append(7)
ls1.append(8)
ls1.append(9)
ls1.append(10)
ls1.append(11)
ls1.append(12)
# print(ls1.is_circular_llist(ls1))

ls2 = linkedList()
ls2.append(1)
ls2.append(2)
ls2.append(3)
ls2.append(4)
ls2.print_list()

print(ls1.is_circular_llist(ls2))
