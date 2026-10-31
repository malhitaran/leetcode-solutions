# Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted 2026-10-31 — Python3, runtime 83 ms, memory 36.6 MB
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        '''
        if num -1 is in not in this set then that means this is a start of the seq

        '''

        seen=set(nums)
        res=0
        for n in list(seen):
            cnt=0
            x=n
            if x-1 not in seen:
                while x in seen:
                    seen.remove(x)
                    cnt+=1
                    x+=1
            res=max(res, cnt)
        return res
