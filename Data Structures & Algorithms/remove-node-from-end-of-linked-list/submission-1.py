# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        # 1,2,3,4 | n = 2
        # ll = 4
        # head = None 
        list_len = 0
        curr = head
        while curr:
            list_len += 1
            curr = curr.next
        
        curr = head
        if n == list_len:
            return head.next

        nodes_traveled = 0
        curr = head
        while nodes_traveled < list_len - n - 1:
            curr = curr.next
            nodes_traveled += 1
        
        curr.next = curr.next.next
        return head
        
