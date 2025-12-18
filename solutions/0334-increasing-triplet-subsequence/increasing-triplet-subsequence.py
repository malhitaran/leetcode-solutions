# Increasing Triplet Subsequence (Medium)
# https://leetcode.com/problems/increasing-triplet-subsequence/
# Accepted 2025-12-18 — Python3, runtime 15 ms, memory 36.9 MB
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        from typing import List
        
        first = float('inf')
        second = float('inf')

        for x in nums:
            if x <= first:
                first = x          # best (smallest) first element so far
            elif x <= second:
                second = x         # best second element > first so far
            else:
                return True        # found x > second > first

        return False
