# Longest Repeating Character Replacement (Medium)
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Accepted 2026-08-13 — Python3, runtime 79 ms, memory 19.7 MB
from collections import defaultdict
import heapq
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        maybe we can see the most frequent character at any point 
        using a heap then doing a sliding window

        so basically we keep a dictionary then heapify it get the most common and and then keep a sum and then minus from teh sum
        '''
        
        ourDict=defaultdict(int)
        maxF,l, best=0,0,0

        for r in range(len(s)):

            ourDict[s[r]]+=1
            maxF=max(maxF, ourDict[s[r]])
            while (r-l+1)-maxF>k:
                ourDict[s[l]]-=1
                l+=1

            best=max(best, r-l+1)
        return best
