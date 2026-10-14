# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tdl 
        # fast pointer, slow pointer start at same inc by diff amounts
        # if fast == null return false
        # else if slow == fast return true


        fast = head
        slow = head

        while fast:
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
