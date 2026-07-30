# Increasing Triplet Subsequence (Medium)
# https://leetcode.com/problems/increasing-triplet-subsequence/
# Accepted 2026-07-30 — Python3, runtime 471 ms, memory 39.3 MB


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        i=float('infinity')
        j=float('infinity')

        for num in nums:
            if num>j and j>i:
                return True
            if num<i:
                i=num
            elif num<j and num>i:
                j=num

            print(i)
            print(j)
        return False
