# Maximum Number of Vowels in a Substring of Given Length (Medium)
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Accepted 2026-10-31 — Python3, runtime 91 ms, memory 19.8 MB
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        '''
        this seems like a sliding window problem where we have k
        we have to i/d and count the vowels
        '''
        l=0
        best=0
        vowels={'a', 'e', 'i', 'o','u'}
        v_count=0

        for r in range(len(s)):
            if r-l+1>k:
                v_count-=1 if s[l] in vowels else 0
                l+=1
            v_count+=1 if s[r] in vowels else 0
            if r-l+1==k:
                best=max(best, v_count)
            
        return best
