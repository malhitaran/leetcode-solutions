# Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
# Accepted 2026-07-03 — Python3, runtime 0 ms, memory 20.3 MB
from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        

        '''
        3:0

        '''



        seen={}


        for i, num in enumerate(nums):

            if target-num in seen:
                return [seen[target-num], i]
            else:

                seen[num]=i
