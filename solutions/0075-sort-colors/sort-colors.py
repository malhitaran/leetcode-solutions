# Sort Colors (Medium)
# https://leetcode.com/problems/sort-colors/
# Accepted 2026-08-16 — Python3, runtime 0 ms, memory 19.1 MB
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        [2,0,2,1,1,0]
        [0,0,1,1,2,2]

        we may have to do 2 swaps because a swap can mean we swap a 0 and a 2 and if we move on before processing the next 2 or 0 then we can skip that case
        '''

        l,index, r=0,0,len(nums)-1

        while index<=r:
            if nums[index]==0:
                nums[l], nums[index]=nums[index], nums[l]
                index+=1
                l+=1
            elif nums[index]==2:
                nums[r], nums[index]=nums[index], nums[r]
                r-=1
            else:
                index+=1
