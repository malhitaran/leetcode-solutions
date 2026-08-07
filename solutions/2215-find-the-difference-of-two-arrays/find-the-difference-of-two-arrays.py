# Find the Difference of Two Arrays (Easy)
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Accepted 2026-08-07 — Python3, runtime 12 ms, memory 19.5 MB
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        res1=set(nums1)
        res2=set(nums2)
        

        

        return [list(res1.difference(res2)), list(res2.difference(res1))]
