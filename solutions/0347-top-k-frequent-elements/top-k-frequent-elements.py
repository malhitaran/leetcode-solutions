# Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/
# Accepted 2026-06-13 — Python3, runtime 1 ms, memory 22.7 MB
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        count dict
        order by count so the value(frequency)
        then slice k output as a list extracitng keys


        [1,1,1,2,2,3]

        1:3
        2:2
        3:1
        
        '''

        x=Counter(nums)
        x=dict(sorted(x.items(), key=lambda x:x[1], reverse=True))
        x=list(x.keys())
        return x[:k]
