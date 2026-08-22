# Maximum Average Subarray I (Easy)
# https://leetcode.com/problems/maximum-average-subarray-i/
# Accepted 2026-08-22 — Python3, runtime 296 ms, memory 29.7 MB
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if k>=len(nums):
            return float(sum(nums)/len(nums))
        else:
            count=float(sum(nums[:k]))
        best=count
        for i in range(k,len(nums)):
            count+=nums[i]
            count-=nums[i-k]
            print(count)
            best=max(count,best)
        return float(best/k)
