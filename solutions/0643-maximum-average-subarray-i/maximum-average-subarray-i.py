# Maximum Average Subarray I (Easy)
# https://leetcode.com/problems/maximum-average-subarray-i/
# Accepted 2026-05-18 — Python3, runtime 55 ms, memory 29.1 MB
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_sum = sum(nums[:k])
        best_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            best_sum = max(best_sum, window_sum)

        return best_sum / k
