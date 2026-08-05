# Maximum Average Subarray I (Easy)
# https://leetcode.com/problems/maximum-average-subarray-i/
# Accepted 2026-08-05 — Python3, runtime 35 ms, memory 29.3 MB
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        '''


        '''

        if len(nums)<=k:
            print(sum(nums))

            return sum(nums)/k
        else:
            prev=sum(nums[:k])
            best=prev
            
     
        

        for i in range(k, len(nums)):

            
            curr=prev-nums[i-k] + nums[i]
            
            if curr>best:
                best=curr

            prev=curr

    
        return float(best/k)
