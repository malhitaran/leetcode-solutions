# Find Minimum in Rotated Sorted Array (Medium)
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Accepted 2026-08-15 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''
        we can see what side is sorted, from that we know the minimum is the l
        then we go to the unsorted side
        '''

        l,r,best=0,len(nums)-1,float('infinity')
        while l<=r:
            mid=(l+r)//2
            best=min(best,nums[mid])
            print(l, mid, r)
            if nums[mid]>=nums[l]:
                best=min(best,nums[l])
                l=mid+1
            else:
                best=min(best,nums[mid])
                r=mid-1
            
        return best
