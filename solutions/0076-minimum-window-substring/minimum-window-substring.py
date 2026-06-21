# Minimum Window Substring (Hard)
# https://leetcode.com/problems/minimum-window-substring/
# Accepted 2026-06-21 — Python3, runtime 138 ms, memory 20 MB

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        seen=Counter(t)
        missing=len(t)
        best=float('infinity')
        l, r =0, 0
        sl, sr=0,0

        while r<len(s):
            letter=s[r]
            #if its in
            print(missing)
            if letter in seen:
                if seen[letter]>0:
                    missing-=1
                seen[letter]-=1
    
            while missing ==0:
                if (r-l+1)<best:
                    best=min(best, r-l+1)
                    sl=l
                    sr=r
                if s[l] in seen:
                    seen[s[l]]+=1
                    if seen[s[l]]>0:
                        missing+=1
                l+=1

            r+=1
    
        return s[sl:sr + 1] if best != float('infinity') else ""
