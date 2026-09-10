# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        tail = dummy
        current = head

        while(current):
            tmp = current.next
            tail = current
            current.next = dummy
            dummy = current
            current = tmp
        return tail