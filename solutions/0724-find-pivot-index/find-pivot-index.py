# Find Pivot Index (Easy)
# https://leetcode.com/problems/find-pivot-index/
# Accepted 2026-08-07 — Python3, runtime 7 ms, memory 20.3 MB
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        '''
        sum left

        sum right

        [1,7,3,6,5,6]

        28-6 22 11



        [-1, -1, -1, -1, -1]

        -5

        -1 -2 -4/2 = -2


        [2,1,-1]
        2
        
        0
        '''


        totalSum=sum(nums)
        prefixSum=0

        for i, num in enumerate(nums):
            if (totalSum-num)/2==prefixSum:
                return i
            else:
                prefixSum+=num
        return -1
