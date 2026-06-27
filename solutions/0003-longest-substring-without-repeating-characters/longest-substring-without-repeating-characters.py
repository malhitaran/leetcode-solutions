# Longest Substring Without Repeating Characters (Medium)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Accepted 2026-06-27 — Python3, runtime 44 ms, memory 19.3 MB
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        
        '''
        "pwwkew"

        w:2

        '''


        ourD=defaultdict()
        l=0
        r=0
        best=0
        while r<len(s):
            
            letter=s[r]
            if letter not in ourD:
                ourD[letter]=1
                print(ourD)
            else:
                ourD[letter]+=1
                while ourD[letter]>1:
                    ourD[s[l]]-=1
                    
                    l+=1

            r+=1
            best=max(best, r-l)
        return best
