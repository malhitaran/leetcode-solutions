# Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
# Accepted 2026-06-21 — Python3, runtime 0 ms, memory 20.3 MB
from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen={}



        for i, num in enumerate(nums):

            need=target-num

            if need in seen:
                return [seen[need], i]
            else:
                seen[num]=i
        return []
