# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # TDL
        # Previous node = None
        # Traverse through linkedlist
        # change where the node is pointing to, aka to the node before them
        # store the next node in a temp variable 
        # self.next = previous node 
        # previous node = self 
        # temp variable to iterate forward


        curr = head
        prev = None
        temp = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        return prev

