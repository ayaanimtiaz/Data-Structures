# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # slow and fast pointer
        # fast pointer starts one place ahead of slow, paces 2 studs at a time slowi s one starts at head
        # reverse linkedlist past it
        # iterate through reg half and changed half
        # change inserts and iterate as per usg

        fast = head
        slow = head
        if fast.next:
            fast = fast.next

        while fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                break 
        
        mid = slow.next 
        slow.next = None
        prev = None
        temp = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp 
        midt = prev
        
        # 1 2 3 and 5 -> 4

        original = None
        reorder = None

        #
        while head and midt:
            original = head.next
            reorder = midt.next
            head.next = midt
            midt.next = original
            midt = reorder
            head = original
        


            



        


        