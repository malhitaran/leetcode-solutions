# Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/
# Accepted 2026-06-12 — Python3, runtime 12 ms, memory 32.5 MB
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        newSet=set()

        for num in nums:

            if num in newSet:
                return True

            else: newSet.add(num)

        return False
