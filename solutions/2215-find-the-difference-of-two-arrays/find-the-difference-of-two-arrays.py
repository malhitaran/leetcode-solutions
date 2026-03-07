# Find the Difference of Two Arrays (Easy)
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Accepted 2026-03-07 — Python3, runtime 11 ms, memory 19.5 MB
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        set1=set(nums1)
        set2=set(nums2)

        return [list(set1-set2), list(set2-set1)]
