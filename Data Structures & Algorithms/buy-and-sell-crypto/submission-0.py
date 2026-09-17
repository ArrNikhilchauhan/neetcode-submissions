class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit=0
        purchased_price=prices[0]
        for x in prices:
            if x<purchased_price:
                purchased_price=x
            else:
                max_profit=max(max_profit,x-purchased_price)
        
        return max_profit
