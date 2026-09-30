# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # prev = None
        # while head copy
        # temp = headcopy.next
        # head.next = prev
        # prev = head
        # headcopy = headcopy.next

        prev = None
        cop = head
        temp = 0

        # none <- 1 <- 2  3 -> 4 -> 5
        # temp = 3
        # cop.next = 1
        # prev = 2
        # cop = 3
        while cop:
            temp = cop.next
            cop.next = prev
            prev = cop
            cop = temp
        
        return prev