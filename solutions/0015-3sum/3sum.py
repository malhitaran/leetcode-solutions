# 3Sum (Medium)
# https://leetcode.com/problems/3sum/
# Accepted 2026-11-01 — Python3, runtime 606 ms, memory 22.2 MB
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        '''
        sort it 

        -4, -1, -1, 0, 1, 2

        which one do we move?? 
        '''

        res=[]
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sum3=a+nums[l]+nums[r]
                if sum3>0:
                    r-=1
                elif sum3<0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
