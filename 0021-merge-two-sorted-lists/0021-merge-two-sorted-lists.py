# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # TDL
        # create a new linkedlist 
        # travel through each list and at each iteration compare the nodes
        # if a node is bigger than the other, create that node and iterate the smaller node forward and keep bigger one forward
        # if one node empties, iterate through the non-none one

        curr_one = list1
        curr_two = list2
        merged = ListNode()
        merged_pointer = merged

        while curr_one and curr_two:
            if curr_one.val > curr_two.val:
                merged_pointer.next = ListNode(curr_two.val)
                merged_pointer = merged_pointer.next
                curr_two = curr_two.next
            else:
                merged_pointer.next = ListNode(curr_one.val)
                merged_pointer = merged_pointer.next
                curr_one = curr_one.next
        
        if curr_one:
            merged_pointer.next = curr_one
        if curr_two:
            merged_pointer.next = curr_two
                
        merged = merged.next
        return merged


