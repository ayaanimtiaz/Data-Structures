"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # tdl
        # can u just build a hashmap where we store the randoms
        # key is the original node
        # we just trace thru it after? and rebuild on a copy

        rebuild = {}
        head_pointer = head

        while head_pointer:
            if rebuild.get(head_pointer, 0) == 0:
                rebuild[head_pointer] = Node(head_pointer.val, rebuild.get(head_pointer.next, 0), rebuild.get(head_pointer.random, 0))
            if head_pointer.next == None:
                rebuild[head_pointer].next = None
            if head_pointer.random == None:
                rebuild[head_pointer].random = None
            head_pointer = head_pointer.next

        for key, values in rebuild.items():
            if values.next == 0:
                values.next = rebuild[key.next]
            if values.random == 0:
                values.random = rebuild[key.random]
            
        
        if head:
            return next(iter(rebuild.values()))
        else:
            return head

