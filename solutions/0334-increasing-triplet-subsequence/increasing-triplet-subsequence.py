# Increasing Triplet Subsequence (Medium)
# https://leetcode.com/problems/increasing-triplet-subsequence/
# Accepted 2026-05-17 — Python3, runtime 45 ms, memory 38.9 MB


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:


        '''

        keep track of the one before and the one before that

        5 1 6

        i 5
        j 1
        '''    

        i=float('inf')
        j=float('inf')

        for x in range(len(nums)):
            if nums[x]>i and nums[x]<j:
                j=nums[x]
            elif nums[x]>i and nums[x]>j:
                return True
            elif nums[x]<i:
                i=nums[x]


        return False
