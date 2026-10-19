# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # tdl
        # fast goes n times forward
        # if they move at the smae rate fast will stop at the end
        # start with a dummy
        # fast will stop right before the end, while slow will stop right before the node we need to remove
        # 
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next