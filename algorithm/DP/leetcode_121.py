# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_price = prices[0]
        for price in prices:
            if price < max_price:
                max_price = price
            elif price > max_price:
                c_profit = price - max_price
                if c_profit > profit:
                    profit = c_profit
        return profit
