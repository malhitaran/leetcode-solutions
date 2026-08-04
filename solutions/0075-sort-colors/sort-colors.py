# Sort Colors (Medium)
# https://leetcode.com/problems/sort-colors/
# Accepted 2026-08-04 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.


        [1,0,2]
         l   r



        [1, 1, 2, 2]
        l.     r  

        [0, 0, 1, 1, 2, 2]
               l     r

        switch

        3 pointers


        """
    
        l, r=0, len(nums)-1

        for curr, num in enumerate(nums):

            while (nums[curr]==0 and curr>l) or (nums[curr]==2 and curr<r):
                if nums[curr]==0 and curr>l:
                    #swap l and curr
                    temp=nums[l]
                    nums[l]=nums[curr]
                    nums[curr]=temp
                    l+=1
                else:
                    #swap r and curr
                    temp=nums[r]
                    nums[r]=nums[curr]
                    nums[curr]=temp
                    r-=1

            

            while l<len(nums) and nums[l]==0:
                l+=1

            while r>-1 and nums[r]==2:
                r-=1
