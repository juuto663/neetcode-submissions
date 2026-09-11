class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        buy, sell = 0, 1
        profit = 0

        while sell < len(prices):
            profit = max(profit, prices[sell] - prices[buy])

            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy + 1
            else:
                sell += 1
            
        return profit

