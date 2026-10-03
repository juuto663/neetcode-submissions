# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        smallest = [(node.val, i, node) for i, node in enumerate(lists) if node] # O(k) space, O(k) time
        heapq.heapify(smallest) # O(k) space, O(k) time

        if not smallest:
            return None
        
        dummy = tail = ListNode()
        while smallest:
            _, i, node = heapq.heappop(smallest)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(smallest, (node.next.val, i, node.next))
            
        return dummy.next



        