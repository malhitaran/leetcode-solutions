# Majority Element (Easy)
# https://leetcode.com/problems/majority-element/
# Accepted 2026-08-04 — Python3, runtime 3 ms, memory 21.3 MB
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        numFreq=Counter(nums)
        most=float('-infinity')
        res=0
        for num,freq in numFreq.items():

            if freq>most:
                res=num
                most=freq

        return res
