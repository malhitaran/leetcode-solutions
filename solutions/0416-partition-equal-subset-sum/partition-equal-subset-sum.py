# Partition Equal Subset Sum (Medium)
# https://leetcode.com/problems/partition-equal-subset-sum/
# Accepted 2026-11-01 — Python3, runtime 304 ms, memory 20.7 MB
class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        ourS=sum(nums)
        if ourS%2 !=0:
            return False
        target=ourS//2
        dp=set()
        dp.add(0)

        
        for i in range(len(nums)-1, -1, -1):
            
            newDp=set()
            for e in dp:
                if nums[i]+ e == target:
                    return True
                newDp.add(nums[i]+ e)
                newDp.add(e)
            dp=newDp
        return False
