class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, max_profit = 0, 0
        for r, p in enumerate(prices):
            if p < prices[l]:
                l = r
            max_profit = max(max_profit, p - prices[l])
        return max_profit