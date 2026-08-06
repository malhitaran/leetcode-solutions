# Maximum Number of Vowels in a Substring of Given Length (Medium)
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Accepted 2026-08-06 — Python3, runtime 126 ms, memory 20 MB
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        '''

        sliding window

        we will have a count, then we know if the next letter is a vowel we will have to recalculate whether its the best, if the last element was a vowel we minus 1 from the count. 


        first process the first k, 


        '''
        vowels={'A','a','E','e','I','i','O','o','U','u'}

        

        #process the first k

        out=0
        for i in range(k):
            if s[i] in vowels:
                out+=1
        best=out
        
        
        for i in range(k, len(s)):
            
            

            if s[i] in vowels:
                out+=1

            if s[i-k] in vowels:
                out-=1
            
            print(out)
            if out>best:
                best=out
        
        

        return best
