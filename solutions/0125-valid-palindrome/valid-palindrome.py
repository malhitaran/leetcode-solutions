# Valid Palindrome (Easy)
# https://leetcode.com/problems/valid-palindrome/
# Accepted 2026-08-13 — Python3, runtime 4 ms, memory 20.3 MB
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        for ch in s:
            if ch.isalnum():
                temp.append(ch)
        s=''.join(temp)
        s=s.lower()
        return s==s[::-1]
