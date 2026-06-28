# Find the Duplicate Number (Medium)
# https://leetcode.com/problems/find-the-duplicate-number/
# Accepted 2026-06-28 — Python3, runtime 11 ms, memory 33.7 MB
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        ourS=set()
        for num in nums:
            if num in ourS:
                return num
            else:
                ourS.add(num)
