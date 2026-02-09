# Max Consecutive Ones III (Medium)
# https://leetcode.com/problems/max-consecutive-ones-iii/
# Accepted 2026-02-09 — Python3, runtime 63 ms, memory 22.5 MB
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        best = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            best = max(best, r - l + 1)

        return best
