# Minimum Window Substring (Hard)
# https://leetcode.com/problems/minimum-window-substring/
# Accepted 2026-08-02 — Python3, runtime 79 ms, memory 19.8 MB

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        '''

        we can go through the string


        '''

        best=float('infinity')
        l,r=0,0
        tFreq=Counter(t)
        missing=sum(tFreq.values())

        lStore,rStore=0,0

        while r<len(s):
            if s[r] in tFreq:
                if tFreq[s[r]]>0:
                    missing-=1
                tFreq[s[r]]-=1
                r+=1
            else:
                r+=1
            while missing==0:
                if r-l+1<best:
                    lStore=l
                    rStore=r
                    best=r-l+1
               
                if s[l] in tFreq:
                    tFreq[s[l]]+=1
                    if tFreq[s[l]]>0:
                        missing+=1
                l+=1
            
            
                            
        return s[lStore:rStore]
