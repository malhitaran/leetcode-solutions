# Increasing Triplet Subsequence (Medium)
# https://leetcode.com/problems/increasing-triplet-subsequence/
# Accepted 2026-04-26 — Python3, runtime 11 ms, memory 38.8 MB
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first=float('inf')
        second=float('inf')
        
        for num in nums:
            if num <=first:
                first=num
            elif num<=second:
                second=num
            else:

                return True

        return False
