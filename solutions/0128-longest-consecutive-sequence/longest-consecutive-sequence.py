# Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted 2026-08-16 — Python3, runtime 35 ms, memory 36.5 MB
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        track=set(nums)
        best=0
        for num in track:
            if num-1 not in track:
                count=num
                while count in track:
                    count+=1
                best=max(best, count-num)
        return best
