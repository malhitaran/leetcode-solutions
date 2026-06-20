# Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/
# Accepted 2026-06-20 — Python3, runtime 3 ms, memory 19.3 MB
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
    
        x=Counter(s)
        t=Counter(t)
        return x==t
