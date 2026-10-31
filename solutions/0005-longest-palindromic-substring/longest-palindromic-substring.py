# Longest Palindromic Substring (Medium)
# https://leetcode.com/problems/longest-palindromic-substring/
# Accepted 2026-10-31 — Python3, runtime 519 ms, memory 19.1 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:

        '''

        seems like we go one by one then expand outwards 

        "cbbd"


        '''
        
        def palindrome_length(l,r):
            nonlocal longest, l_string, curr
            while (l>=0 and r<len(s)) and (s[l]==s[r]):
                curr=r-l+1
                if curr>longest:
                    longest=curr
                    l_string=s[l:r+1]
                r+=1
                l-=1
          

            
        longest=0
        l_string=""

        for i in range(len(s)):
            curr=0

            #adjust l and r
            #even
            #do we want to go left or right
            palindrome_length(i,i)
            
            palindrome_length(i-1, i)

            #odd
            palindrome_length(i-1, i+1)

        return l_string
