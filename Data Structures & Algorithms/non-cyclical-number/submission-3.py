class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sum_of_squares(n)

        while slow != fast:
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(fast)
            fast = self.sum_of_squares(fast)
            
        return True if fast == 1 else False
    
    def sum_of_squares(self, n: int) -> int:
        ret = 0
        while n:
            last_digit = n % 10
            ret += (last_digit ** 2)
            n = n // 10
        
        return ret