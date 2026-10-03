# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        next_smallest = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(next_smallest, (node.val, i, node))

        if not next_smallest:
            return None

        dummy = ListNode(0, next_smallest[0][2])
        while next_smallest:
            val, l, node = heapq.heappop(next_smallest)
            if node.next:
                heapq.heappush(next_smallest, (node.next.val, l, node.next))
            node.next = next_smallest[0][2] if next_smallest else None
        
        return dummy.next




        