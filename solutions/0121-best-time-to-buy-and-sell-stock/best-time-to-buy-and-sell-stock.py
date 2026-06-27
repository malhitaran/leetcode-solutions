# Best Time to Buy and Sell Stock (Easy)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted 2026-06-27 — Python3, runtime 78 ms, memory 28.5 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''

        [7,1,5,3,6,4]

        [7,6,4,3,1]

        if num is less than or equalour less
            we move our left to right
    

        if num is greater than we calcualte new best and keep going
        '''

        left=0
        right=0
        best=0
        while right<len(prices):
            
            if prices[right]>prices[left]:
                best=max(best, prices[right]-prices[left])
            else:
                left=right

            right+=1
            

        return best
