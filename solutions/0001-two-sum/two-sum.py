# Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
# Accepted 2026-07-31 — Python3, runtime 3 ms, memory 20.5 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        seen=dict()

        for i,num in enumerate(nums):
            if target-num in seen:
                return [i, seen[target-num]]
            if num in seen:
                continue
            seen[num]=i
