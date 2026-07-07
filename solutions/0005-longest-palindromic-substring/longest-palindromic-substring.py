# Longest Palindromic Substring (Medium)
# https://leetcode.com/problems/longest-palindromic-substring/
# Accepted 2026-07-07 — Python3, runtime 283 ms, memory 19.3 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:


        '''
        so we have to expand from the middle

        best case is on squared

        so we go through each letter and expand outwards
        '''
            

        resLen=0
        res=""
        for i in range(len(s)):

            l,r=i,i

            while l>=0 and r<len(s) and s[l]==s[r]:

                if r-l+1>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1

            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:

                if r-l+1>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1

        return res
