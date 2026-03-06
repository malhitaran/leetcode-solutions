# Find Pivot Index (Easy)
# https://leetcode.com/problems/find-pivot-index/
# Accepted 2026-03-06 — Python3, runtime 7 ms, memory 20.4 MB
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i
            
            left_sum += nums[i]

        return -1
