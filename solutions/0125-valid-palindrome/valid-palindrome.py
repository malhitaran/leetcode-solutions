# Valid Palindrome (Easy)
# https://leetcode.com/problems/valid-palindrome/
# Accepted 2026-08-13 — Python3, runtime 7 ms, memory 20.7 MB
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = re.sub(r"[^a-zA-Z0-9]", "", s)

        cleaned=cleaned.lower()
        print(cleaned)
        print(cleaned[::-1])
        return cleaned==cleaned[::-1]
