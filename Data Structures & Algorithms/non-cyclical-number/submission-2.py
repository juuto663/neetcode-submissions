class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            n = self.sum_of_squares(n)
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.add(n)
    
    def sum_of_squares(self, n: int) -> int:
        ret = 0
        while n:
            last_digit = n % 10
            ret += (last_digit ** 2)
            n = n // 10
        
        return ret