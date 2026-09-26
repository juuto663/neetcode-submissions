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
            tmp = curr.next
            new_node = Node(curr.val, None, Node(-10000, None, None))
            curr.next = new_node
            new_node.next = tmp
            curr = curr.next.next if curr.next else None

        curr = head
        while curr:
            copy = curr.next
            copy.random = curr.random.next if curr.random else None
            curr = curr.next.next if curr.next else None

        curr = head
        ret_node = head.next
        while curr:
            copy = curr.next
            orig_next = curr.next.next if curr.next else None
            curr.next = orig_next
            copy.next = orig_next.next if orig_next else None
            curr = curr.next


        return ret_node