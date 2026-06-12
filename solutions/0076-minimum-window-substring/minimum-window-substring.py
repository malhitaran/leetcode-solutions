# Minimum Window Substring (Hard)
# https://leetcode.com/problems/minimum-window-substring/
# Accepted 2026-06-12 — Python3, runtime 55 ms, memory 19.7 MB
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        '''

        if t is greater than return ""

        sliding window with sets?

        two pointers then reduce(need to keep track of set)
        '''
        counts={}
        for char in t:
            counts[char]=counts.get(char,0)+1

        left=0
        best=float('inf')
        finalL=0
        finalR=0
        missing = len(t)

        for right in range(len(s)):
            if s[right] not in counts:
                continue

            if s[right] in counts:
                if counts[s[right]]>0:
                    missing-=1
                counts[s[right]]-=1

            while missing ==0:
                if right - left + 1 < best:
                    best = right - left + 1
                    finalL = left
                    finalR = right
                
                if s[left] in counts:
                    counts[s[left]]+=1
                    if counts[s[left]]>0:
                        missing+=1
                    
            
                left+=1

        if best == float('inf'):
            return ""

        return s[finalL:finalR + 1]
