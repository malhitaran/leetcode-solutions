# Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted 2026-08-01 — Python3, runtime 49 ms, memory 36.7 MB
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        '''
        we know that they all start from a point

        - the big key. its at the beginning if n-1 doesnt exist in the set!!!!
        '''

        ourS=set(nums)
        best=0
        curr=1
        for num in ourS:
            curr=1
           
            if num-1 not in ourS:
                while num+1 in ourS:
                    curr+=1
                    num=num+1
                best=max(best,curr)
        return best
