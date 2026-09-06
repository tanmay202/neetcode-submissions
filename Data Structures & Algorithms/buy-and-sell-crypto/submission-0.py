class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_p=0
        for price in prices:
            min_price=min(price,min_price)
            profit=price-min_price
            max_p=max(max_p,profit)
        return max_p