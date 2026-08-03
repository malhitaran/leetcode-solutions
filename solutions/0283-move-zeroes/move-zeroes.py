# Move Zeroes (Easy)
# https://leetcode.com/problems/move-zeroes/
# Accepted 2026-08-03 — Python3, runtime 3 ms, memory 20.5 MB
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.


        so my right will find non numbers

        so we can have a left pointer that finds a zero
        right pointer that finds non zero


        """
        l, r=0,0

        while r<len(nums):

            
            if nums[r]!=0 and nums[l]==0 and l<r:
                #swap
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp
                l+=1
                r+=1
            elif nums[r]==0:
                r+=1
            elif nums[l]!=0:
                l+=1
                r+=1
        return nums
