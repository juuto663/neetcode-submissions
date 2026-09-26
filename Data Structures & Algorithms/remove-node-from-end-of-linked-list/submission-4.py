# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        len_list = 0
        curr = head 
        while curr:
            len_list += 1
            curr = curr.next
        
        if len_list == n:
            return head.next
        
        nodes_to_travel = len_list - n - 1
        curr = head
        for _ in range(nodes_to_travel):
            curr = curr.next
        
        curr.next = curr.next.next

        return head