# Maximum Subarray (Medium)
# https://leetcode.com/problems/maximum-subarray/
# Accepted 2026-11-01 — Python3, runtime 36 ms, memory 31.4 MB
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        '''
        dp solution

        from my index, does going foward help me

        actually from my index does inclduing the previous sum help me or not 

        does including the prev best sum help me or nah?? 
        keep track of that 


        '''

        curSum=float('-infinity')
        res=float('-infinity')
        for n in nums:
            curSum=max(n, n+curSum)

            res=max(res, curSum)
        return res
