# Permutation in String (Medium)
# https://leetcode.com/problems/permutation-in-string/
# Accepted 2026-06-27 — Python3, runtime 29 ms, memory 19.5 MB
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
        s1 = "ab", s2 = "eidbaooo"

        '''
        s1C=Counter(s1)
        l=0
        s2C={}

        for r in range(len(s2)):
            if s2[r] in s1C:
                s2C[s2[r]]=1+ s2C.get(s2[r], 0)
                while s2C[s2[r]]>s1C[s2[r]]:
                    s2C[s2[l]]-=1
                    l+=1
            else:
                s2C={}
                l=r+1
            
            if s1C==s2C:
                return True

            
        return False
