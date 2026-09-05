# Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted 2026-09-05 — Python3, runtime 59 ms, memory 36.6 MB
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        best,i=0,0
        while seen:
            x=nums[i]
            if x-1 in seen:
                i+=1
                continue
            else:
                while x in seen:
                    seen.remove(x)
                    x+=1
                best=max(best, x-nums[i])
                i+=1
        return best
