# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final_sum = [] # O(max(l1, l2))
        carry = False
        while l1 or l2:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0
            
            node_sum = l1_num + l2_num + 1 if carry else l1_num + l2_num
            carry = node_sum > 9
            node_sum %= 10
            final_sum.append(node_sum)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            final_sum.append(1)

        print(final_sum)
        
        dummy = ListNode()
        prev = dummy
        for num in final_sum:
            curr = ListNode(num, None)
            prev.next = curr
            prev = curr
        
        return dummy.next
        



