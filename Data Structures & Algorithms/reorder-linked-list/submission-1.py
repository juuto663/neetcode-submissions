# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_map = {}
        index = 0
        back_to_head = head
        while head:
            node_map[index] = head
            head = head.next
            index += 1
        
        num_nodes = len(node_map)
        head = back_to_head
        for i in range(1, num_nodes):
            if i % 2 == 1:
                head.next = node_map[num_nodes - (i + 1) / 2]
            else:
                head.next = node_map[i / 2]
            head = head.next
        head.next = None

