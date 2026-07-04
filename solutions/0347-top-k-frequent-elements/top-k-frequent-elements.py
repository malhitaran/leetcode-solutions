# Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/
# Accepted 2026-07-04 — Python3, runtime 7 ms, memory 22.9 MB
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        


        numFrequency=Counter(nums)

        heap=[]

        for num, count in numFrequency.items():

            heapq.heappush(heap, (count, num))

            if len(heap)>k:
                heapq.heappop(heap)

        return [num for count, num in heap]
