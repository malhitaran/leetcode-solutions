# Find Minimum in Rotated Sorted Array (Medium)
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Accepted 2026-08-15 — Python3, runtime 0 ms, memory 19.5 MB
class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''
        we can see what side is sorted, from that we know the minimum is the l
        then we go to the unsorted side
        '''

        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
            
        return nums[l]
