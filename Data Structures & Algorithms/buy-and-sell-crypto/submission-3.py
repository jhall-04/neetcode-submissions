class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        max_profit = 0
        cur_min = float('inf')
        while r < len(prices):
            if cur_min > prices[r]:
                cur_min = prices[r]
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        return max_profit
            



            
        