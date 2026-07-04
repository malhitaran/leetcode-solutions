# Kth Largest Element in an Array (Medium)
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Accepted 2026-07-04 — Python3, runtime 113 ms, memory 31.7 MB
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        nums=[-x for x in nums]

        
        heapq.heapify(nums)

        for i in range(k):


            x=heapq.heappop(nums)

        return -x
