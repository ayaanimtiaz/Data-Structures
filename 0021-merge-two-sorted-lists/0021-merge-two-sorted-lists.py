# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        merged =  ListNode()
        dummy = merged
        cap_one = list1
        cap_two = list2


        while cap_one and cap_two:
            if cap_one.val >= cap_two.val:
                dummy.next = ListNode(cap_two.val)
                cap_two = cap_two.next
            else:
                dummy.next = ListNode(cap_one.val)
                cap_one = cap_one.next
            dummy = dummy.next

        while cap_two:
            dummy.next = ListNode(cap_two.val)
            cap_two = cap_two.next
            dummy = dummy.next

        while cap_one:
            dummy.next = ListNode(cap_one.val)
            cap_one = cap_one.next
            dummy = dummy.next

        merged = merged.next

        
        return merged
        




