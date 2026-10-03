# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, obj):
        return self.val < obj.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []

        for l in lists:
            curr = l
            while curr:
                heapq.heappush(heap, curr)
                curr = curr.next

        if not heap:
            return None

        head = heap[0] 
        while heap:
            next_node = heapq.heappop(heap)
            next_node.next = heap[0] if heap else None
        
        return head



            
        