# Move Zeroes (Easy)
# https://leetcode.com/problems/move-zeroes/
# Accepted 2026-02-06 — Python3, runtime 8 ms, memory 20.6 MB
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        


        from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  # next index to place a non-zero

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:              
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1

        #10023201
        #12003201
        #12300201
        #12321000
