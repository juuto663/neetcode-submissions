class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        profit = 0
        buy_day, sell_day = 0, 1
        while sell_day < len(prices):
            profit = max(profit, prices[sell_day] - prices[buy_day])

            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day
                sell_day = buy_day + 1
            else:
                sell_day += 1
        
        return profit