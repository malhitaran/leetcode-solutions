# Reverse Words in a String (Medium)
# https://leetcode.com/problems/reverse-words-in-a-string/
# Accepted 2026-05-16 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def reverseWords(self, s: str) -> str:

        s=s.split()
        
        s.reverse()

        return ' '.join(s)
