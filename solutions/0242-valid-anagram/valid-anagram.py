# Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/
# Accepted 2026-06-12 — Python3, runtime 7 ms, memory 19.9 MB
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        
        counts1=list(s)

        counts1=Counter(counts1)

        counts2=list(t)

        counts2=Counter(counts2)
        
        return counts2==counts1
