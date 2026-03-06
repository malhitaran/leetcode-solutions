# Longest Subarray of 1's After Deleting One Element (Medium)
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Accepted 2026-03-06 — Python3, runtime 48 ms, memory 24.4 MB
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros=0
        l=0
        best=0

        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            
            while zeros>1:
                if nums[l]==0:
                    zeros-=1
                l+=1
            best=max(best, r-l)

        return best
