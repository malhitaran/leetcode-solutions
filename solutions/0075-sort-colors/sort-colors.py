# Sort Colors (Medium)
# https://leetcode.com/problems/sort-colors/
# Accepted 2026-08-16 — Python3, runtime 0 ms, memory 19.2 MB
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

        while index<len(nums):
            while l<len(nums) and nums[l]==0:
                l+=1
            while r>-1 and nums[r]==2:
                r-=1
            while (nums[index]==2 and r>index) or (nums[index]==0 and l<index):
                if nums[index]==0:
                    #swap with left
                    tmp=nums[index]
                    nums[index]=nums[l]
                    nums[l]=tmp
                    l+=1
                else:
                    tmp=nums[index]
                    nums[index]=nums[r]
                    nums[r]=tmp
                    r-=1
    
            index+=1
