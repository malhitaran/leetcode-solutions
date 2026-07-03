# Longest Substring Without Repeating Characters (Medium)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Accepted 2026-07-03 — Python3, runtime 19 ms, memory 19.3 MB

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        '''


        '''
        

        seen=defaultdict(int)

        l=0
        r=0
        best=0

        while r<len(s):

            seen[s[r]]+=1

            while seen[s[r]]>1:
                seen[s[l]]-=1
                l+=1
            
            best=max(best, r-l+1)
            r+=1

        
        return best
