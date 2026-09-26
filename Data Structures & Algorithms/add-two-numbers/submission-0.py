# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = self.craft_num(l1) 
        num_2 = self.craft_num(l2)
        sum_of_lists = num_1 + num_2
        places = len(str(sum_of_lists))
        
        ret = ListNode()
        phone_home = ret
        i = 1
        while i <= places:
            ret.next = ListNode((sum_of_lists % (10 ** i)) // (10 ** (i - 1)))
            ret = ret.next
            i += 1
        
        return phone_home.next

    
    def craft_num(self, l1: ListNode) -> int:
        num = 0
        nodes_traveled = 0
        while l1:
            num += (l1.val * (10 ** nodes_traveled))
            l1 = l1.next
            nodes_traveled += 1
        return num