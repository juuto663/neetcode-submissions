class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        l, r = 0, 1

        profit = 0
        while r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1        
        if profit < 0:
            return 0
        return profit