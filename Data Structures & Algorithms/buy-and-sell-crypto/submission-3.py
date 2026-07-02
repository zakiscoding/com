class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices:
            if buy>price:
                buy=price
            profit = max(profit, price-buy)
        return profit