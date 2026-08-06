# Maximum Number of Vowels in a Substring of Given Length (Medium)
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Accepted 2026-08-06 — Python3, runtime 83 ms, memory 19.8 MB
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        '''

        sliding window

        we will have a count, then we know if the next letter is a vowel we will have to recalculate whether its the best, if the last element was a vowel we minus 1 from the count. 


        first process the first k, 


        '''
        vowels={'A','a','E','e','I','i','O','o','U','u'}

        
        l, cnt, res=0,0,0

        for r in range(len(s)):

            cnt+=1 if s[r] in vowels else 0

            if r-l+1>k:
                cnt-=1 if s[l] in vowels else 0
                l+=1
            
            res=max(res, cnt)

        return res
