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
        if not head:
            return None

        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            tmp = curr.next
            curr.next = new_node
            new_node.next = tmp
            curr = curr.next.next
        
        curr = head
        while curr:
            copy = curr.next
            copy.random = curr.random.next if curr.random else None
            curr = curr.next.next
    
        curr = head
        ret_head = curr.next
        while curr:
            copy = curr.next

            orig_next = curr.next.next
            curr.next = orig_next
            copy.next = orig_next.next if orig_next else None

            curr = curr.next if curr else None
        
        return ret_head
        
