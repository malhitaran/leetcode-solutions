# Find the Difference of Two Arrays (Easy)
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Accepted 2026-03-07 — Python3, runtime 450 ms, memory 19.5 MB
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        output=[]
        diff1=[]
        diff2=[]

        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in diff1:
                diff1.append(nums1[i])

        for j in range(len(nums2)):
            if nums2[j] not in nums1 and nums2[j] not in diff2:
                diff2.append(nums2[j])

        output.append(diff1)
        output.append(diff2)

        return output
