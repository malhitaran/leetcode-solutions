# Valid Palindrome (Easy)
# https://leetcode.com/problems/valid-palindrome/
# Accepted 2026-06-20 — Python3, runtime 7 ms, memory 20.6 MB
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''
        we can remove all non alphanumeric characters
        then compare the reverse

        or we can have a pointer to the front, pointer to the back if its not a alphanumeric then we move the pointer, and we continually compare, if there not equal on a alpha numeric we return false

        we got two options here, we can try convert to alphanumeric then compare

        or we can compare and skip past non alpha numerics
        '''
        x=re.sub(r"[^a-zA-Z0-9]", "",s)
        x=x.lower()
        
        start=0
        end=len(x)-1

        while start<end:
            if x[start]!=x[end]:
                return False
            start+=1
            end-=1
        return True
