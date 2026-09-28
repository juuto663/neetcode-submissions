# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        carry = False
        while l1 or l2:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0
            
            node_sum = l1_num + l2_num + 1 if carry else l1_num + l2_num
            carry = node_sum > 9
            node_sum %= 10
            
            curr = ListNode(node_sum, None)
            prev.next = curr
            prev = curr

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            prev.next = ListNode(1, None)
        
        return dummy.next

        



