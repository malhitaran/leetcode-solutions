# Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
# Accepted 2026-06-12 — Python3, runtime 3 ms, memory 20.3 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i
