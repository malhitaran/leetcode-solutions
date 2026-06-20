# Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/
# Accepted 2026-06-20 — Python3, runtime 11 ms, memory 32.2 MB
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        output=set()
        for num in nums:
            if num in output:
                return True
            output.add(num)
        return False
