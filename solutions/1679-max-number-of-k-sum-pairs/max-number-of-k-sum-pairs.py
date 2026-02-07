# Max Number of K-Sum Pairs (Medium)
# https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Accepted 2026-02-07 — Python3, runtime 457 ms, memory 31.5 MB
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations=0
        lhs=0
        rhs=len(nums)-1
        nums.sort()

        while lhs<rhs:
            sum=nums[lhs]+nums[rhs]
            if sum==k:
                operations+=1
                rhs-=1
                lhs+=1
            elif sum<k:
                lhs+=1
            else:
                rhs-=1

        return operations
