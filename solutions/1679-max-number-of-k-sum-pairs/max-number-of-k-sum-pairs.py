# Max Number of K-Sum Pairs (Medium)
# https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Accepted 2026-05-18 — Python3, runtime 472 ms, memory 32.4 MB

from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        '''

        using dict
        '''

        collect=defaultdict(int)
        ops=0
        
        for num in nums:
            need=k-num

            if collect[need]>0:
                ops+=1
                collect[need]-=1
            else:
                collect[num]+=1
        return ops
