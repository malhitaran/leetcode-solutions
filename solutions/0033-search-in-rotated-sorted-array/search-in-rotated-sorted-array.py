# Search in Rotated Sorted Array (Medium)
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Accepted 2026-07-04 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
        binary search

        5

        [5,6,7,0,1,2,4]

        '''
        

        l,r=0, len(nums)-1

        while l<=r:

            mid=(l+r)//2

            if target==nums[mid]:
                return mid

            #if were in the left
            if nums[mid]>=nums[l]:

                if target>nums[mid] or target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1




            #if were in the right
            else:
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
