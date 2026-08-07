# Find the Difference of Two Arrays (Easy)
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Accepted 2026-08-07 — Python3, runtime 13 ms, memory 19.5 MB
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        res1=set(nums1)
        res2=set(nums2)
        

        for num2 in nums2:
            if num2 in res1:
                res1.remove(num2)

        for num1 in nums1:
            if num1 in res2:
                res2.remove(num1)

        return [list(res1), list(res2)]
