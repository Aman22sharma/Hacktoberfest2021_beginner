# AUTHOR: Bar Lerer
# Python3 Concept: Algorithm to find if there is a circle in a singly linked list, and returns the start of that cycle
# GITHUB: https://github.com/Barlerer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return None
        slow = head
        fast = head
        
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while (slow!=fast):
                    fast=fast.next
                    slow=slow.next
                return fast
        return None
        