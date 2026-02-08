# Maximum Number of Vowels in a Substring of Given Length (Medium)
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Accepted 2026-02-08 — Python3, runtime 63 ms, memory 19.7 MB
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels=["a","e","i","o","u"]
        current=0
        
        for i in range(k):
            if s[i] in vowels:
                current+=1
        max=current
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                current-=1
            if s[i] in vowels:
                current+=1
            if current>max:
                max=current
        
        return max
