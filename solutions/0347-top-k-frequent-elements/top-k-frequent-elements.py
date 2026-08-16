# Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/
# Accepted 2026-08-16 — Python3, runtime 7 ms, memory 25.1 MB
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        going to do it the bucket way now

        so we get the frequency 

        then we store it in that respective frequency bucket
        '''

        bucket=[[] for _ in range(len(nums))]
        res=[]
        numFreq=Counter(nums)  

        
        for num, freq in numFreq.items():
            
            bucket[freq-1].append(num)
        
        for i in range(len(bucket)-1, -1, -1):
           
            for item in bucket[i]:
                res.append(item)
                k-=1
                if k==0:
                    return res
