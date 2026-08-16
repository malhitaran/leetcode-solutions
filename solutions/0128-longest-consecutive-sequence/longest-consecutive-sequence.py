# Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted 2026-08-16 — Python3, runtime 70 ms, memory 36.7 MB
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        '''
        if there is no n-1 in the set then we know its a start, we can increment the count and then look for the next item 

        

   
        '''

        track=set(nums)
        best=0
        for num in nums:
            count=0
            if num-1 not in track:
                while num in track:
                    track.remove(num)
                    num+=1
                    count+=1
                best=max(best, count)
            else:
                continue

        return best
