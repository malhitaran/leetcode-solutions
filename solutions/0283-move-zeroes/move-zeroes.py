# Move Zeroes (Easy)
# https://leetcode.com/problems/move-zeroes/
# Accepted 2026-05-18 — Python3, runtime 0 ms, memory 20.6 MB
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.






        [0,1,0,3,12]


        0    non 0.  swap
        0.   0.   increment secondPointer
        non 0.    0.   firstPointer=secondPointer
        non 0.    non 0.   increment both
        """
        
        left=0
        

        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left], nums[right]= nums[right], nums[left]
                left+=1
