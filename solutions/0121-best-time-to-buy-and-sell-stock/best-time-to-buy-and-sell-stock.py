# Best Time to Buy and Sell Stock (Easy)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted 2026-08-05 — Python3, runtime 31 ms, memory 28.5 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        if its decreasing replace my low

        if its increasing recalculate my best



        '''
        low=float('infinity')
        best=0
        for price in prices:
            if price <low:
                low=price

            if price>low:
                best=max(best, price-low)

        return best
