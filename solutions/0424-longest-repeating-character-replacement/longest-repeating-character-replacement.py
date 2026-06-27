# Longest Repeating Character Replacement (Medium)
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Accepted 2026-06-27 — Python3, runtime 144 ms, memory 19.7 MB
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''

        "AABABBA"


        '''
        count={}
        l=0

        res=0

        for r in range(len(s)):

            count[s[r]]=1+count.get(s[r], 0)

            while (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            
            res=max(res, r-l+1)
        return res
