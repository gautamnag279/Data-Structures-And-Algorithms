class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        profit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                totalProfit += profit
        return totalProfit
