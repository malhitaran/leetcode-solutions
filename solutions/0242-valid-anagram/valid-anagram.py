# Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/
# Accepted 2026-06-12 — Python3, runtime 11 ms, memory 19.5 MB
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        counts1={}

        for char in s:
            counts1[char]=counts1.get(char, 0)+1


        counts2={}

        for char in t:
            counts2[char]=counts2.get(char, 0)+1
            
        return counts2==counts1
