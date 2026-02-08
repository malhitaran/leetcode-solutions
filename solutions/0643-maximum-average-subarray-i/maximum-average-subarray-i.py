# Maximum Average Subarray I (Easy)
# https://leetcode.com/problems/maximum-average-subarray-i/
# Accepted 2026-02-08 — Python3, runtime 57 ms, memory 29.6 MB
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        #[1,12,-5,-6,50,3]
        
        window_sum=sum(nums[:k])
        window_max=window_sum

        for i in range(k, len(nums)):
            window_sum+=nums[i]-nums[i-k]
            if window_sum>window_max:
                window_max=window_sum
            
        return window_max/k
