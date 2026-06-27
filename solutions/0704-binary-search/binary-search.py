# Binary Search (Easy)
# https://leetcode.com/problems/binary-search/
# Accepted 2026-06-27 — Python3, runtime 0 ms, memory 20.5 MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start=0
        end=len(nums)-1
                
        while start<=end:
            midpoint=((end-start)//2)+start
            if nums[midpoint]==target:
                return midpoint
            elif nums[midpoint]>target:
                end=midpoint-1
            else:
                start=midpoint+1

        return -1
