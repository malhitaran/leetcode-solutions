# Product of Array Except Self (Medium)
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted 2026-04-26 — Python3, runtime 12 ms, memory 25.7 MB
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        new=[0]*len(nums)
        cal=1
        for i in range(len(nums)):
            new[i]=cal
            cal*=nums[i]
        
        cal=1
        for i in range(len(nums)-1 , -1, -1):
            new[i]=cal*new[i]
            cal*=nums[i]
            
        return new
