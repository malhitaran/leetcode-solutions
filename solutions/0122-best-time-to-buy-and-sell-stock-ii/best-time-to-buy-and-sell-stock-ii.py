# Best Time to Buy and Sell Stock II (Medium)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Accepted 2026-08-05 — Python3, runtime 2 ms, memory 20.4 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        [3,3,5,0,0,3,1,4]


        '''
        profit=0

        for i in range(1, len(prices)):

            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]

        return profit
