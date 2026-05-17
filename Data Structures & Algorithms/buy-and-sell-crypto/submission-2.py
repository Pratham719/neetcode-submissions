class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimmum_price = prices[0]
        max_profit = 0
        
        for price in prices:
            minimmum_price = min(minimmum_price, price)

            profit = price - minimmum_price

            max_profit = max(max_profit, profit)

        return max_profit
