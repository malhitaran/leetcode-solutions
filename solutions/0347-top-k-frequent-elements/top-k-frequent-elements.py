# Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/
# Accepted 2026-08-16 — Python3, runtime 3 ms, memory 23 MB
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        going to do it the heap way first
        '''

        
        numFreq=Counter(nums)
        heap=[]
        res=[]
        for num, freq in numFreq.items():
            heap.append((-freq,num))

        heapq.heapify(heap)
        print(heap)

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
