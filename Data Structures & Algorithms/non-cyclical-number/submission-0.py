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
        for num in str(n):
            ret += (int(num) ** 2)
        
        return ret