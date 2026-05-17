class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimmum_price=prices[0]
        profit=0
        max_profit=0
        max_=0
        for i in range(len(prices)):
            if prices[i]<minimmum_price:
                minimmum_price=prices[i]
            profit=prices[i]-minimmum_price
            
            if profit>max_profit:
                max_profit=profit
        return max_profit