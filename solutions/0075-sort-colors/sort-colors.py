# Sort Colors (Medium)
# https://leetcode.com/problems/sort-colors/
# Accepted 2026-08-04 — Python3, runtime 0 ms, memory 19.5 MB
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.



        """
    
        colourFreq=Counter(nums)

        x=0
        for i in range(3):

            while colourFreq[i]>0:
                
                print(x)
                nums[x]=i
                x+=1
                colourFreq[i]-=1

        return nums
