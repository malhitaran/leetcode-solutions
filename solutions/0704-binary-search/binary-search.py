# Binary Search (Easy)
# https://leetcode.com/problems/binary-search/
# Accepted 2026-06-27 — Python3, runtime 0 ms, memory 20.4 MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start=0
        end=len(nums)-1

        midpoint=((end-start)//2)+start
        while start<=end:
            
            print(start)
            print(end)
            print(midpoint)
            
            if nums[midpoint]==target:
                return midpoint

            elif nums[midpoint]>target:
                end=midpoint-1
                midpoint=((end-start)//2)+start

            else:
                start=midpoint+1
                midpoint=((end-start)//2)+start
        return -1
