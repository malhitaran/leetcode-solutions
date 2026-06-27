# Search in Rotated Sorted Array (Medium)
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Accepted 2026-06-27 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''

        '''

        lo=0
        hi=len(nums)-1

        while lo<=hi:
            mid=(lo+hi)//2

            if nums[mid]==target:
                return mid

            #left side
            if nums[mid]>=nums[lo]:
                if target<nums[lo] or target>nums[mid]:
                    lo=mid+1
                else:
                    hi=mid-1
            #right side
            else:
                if target>nums[hi] or target<nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1
        return -1
