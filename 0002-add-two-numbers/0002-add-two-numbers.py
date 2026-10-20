# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # global sum
        # loop thru each
        dummy = ListNode()
        dummy_pointer = dummy
        curr1 = l1  
        curr2 = l2
        carry = 0
        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            dummy_pointer.next = ListNode(val)
            dummy_pointer = dummy_pointer.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        if carry != 0:
            dummy_pointer.next = ListNode(carry)

        return dummy.next






