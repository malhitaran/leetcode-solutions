# Search in Rotated Sorted Array (Medium)
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Accepted 2026-08-15 — Python3, runtime 0 ms, memory 19.2 MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
        binary search

        5

        [5,6,7,0,1,2,4]

        '''
        

        start,end=0, len(nums)-1

        while start<=end:
            mid=(start+end)//2
            if target==nums[mid]:
                return mid

            
            #if right is sorted
            if nums[mid]<nums[end]:
                if target<=nums[end] and target>=nums[mid]:
                    start=mid+1
                else:
                    end=mid-1
            else:
                if target<=nums[mid] and target>=nums[start]:
                    end=mid-1
                else:
                    start=mid+1

        return -1
