# Find Minimum in Rotated Sorted Array (Medium)
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Accepted 2026-06-27 — Python3, runtime 0 ms, memory 19.3 MB
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        we can find out if its flipped or not

        '''
        
        lo=0
        hi=len(nums)-1
        best = float('inf')
        while lo<=hi:
            mid=((hi-lo)//2)+lo
            if nums[mid]>nums[hi]:
                
                lo=mid+1
            else:
                best = min(best, nums[mid])
                hi=mid-1
        return best
