# Is Subsequence (Easy)
# https://leetcode.com/problems/is-subsequence/
# Accepted 2026-05-18 — Python3, runtime 0 ms, memory 19.3 MB
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i=0

        for char in t:
            if i<len(s) and char==s[i]:
                i+=1
        return i==len(s)
