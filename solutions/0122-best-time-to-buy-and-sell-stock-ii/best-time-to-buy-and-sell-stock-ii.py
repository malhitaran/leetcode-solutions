# Best Time to Buy and Sell Stock II (Medium)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Accepted 2026-08-05 — Python3, runtime 0 ms, memory 20.4 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        [1,2,3,4,5]

        l:
        h:5
           c
        '''


        low, h=prices[0], 0
        profit=0
        for curr in prices:

            if curr<h:
                if h>low:
                    profit+=h-low
                low =curr
                h=curr
            
            if curr>=h:
                h=curr

        if h>low and h==curr:
            profit+=h-low
        return profit
