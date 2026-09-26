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
        orig_to_copy = {}

        curr = head
        ret_head = None
        while curr:
            if not curr in orig_to_copy:
                orig_to_copy[curr] = Node(curr.val, None, None)
                ret_head = orig_to_copy[curr]
            if curr.next:
                if not curr.next in orig_to_copy:
                    orig_to_copy[curr.next] = Node(curr.next.val, None, None)
                orig_to_copy[curr].next = orig_to_copy[curr.next]
            if curr.random:
                if not curr.random in orig_to_copy:
                    orig_to_copy[curr.random] = Node(curr.random.val, None, None)
                orig_to_copy[curr].random = orig_to_copy[curr.random]
            curr = curr.next

        return ret_head