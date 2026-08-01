# Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/
# Accepted 2026-08-01 — Python3, runtime 0 ms, memory 23 MB
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''

        heap question

        so we get the counts, then we store as a list tuple with -count and then the item then add 1 to it and push it back onto the heap 

        '''
        
        numFreq=Counter(nums)
        heap=[]
        for num, count in numFreq.items():
            if len(heap)==k:
                heapq.heappushpop(heap, (count, num))
            else:
                heapq.heappush(heap, (count, num))

        return [item[1] for item in heap]
