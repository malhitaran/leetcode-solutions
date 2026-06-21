# Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
# Accepted 2026-06-21 — Python3, runtime 8 ms, memory 20.8 MB
from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        '''
        [2,7,11,15]

        2: 0
        7:1
        11:2
        ...
        '''
        ourD=dict()

        for i in range(len(nums)):
            if nums[i] in ourD:
                ourD[nums[i]].append(i)
            else:
                ourD[nums[i]]=[i]

        
        for i, num in enumerate(nums):
            need=target-num

            if need in ourD:
                for x in ourD[need]:
                    if x==i:
                        continue
                    else:
                        return[i, x]

        return False
