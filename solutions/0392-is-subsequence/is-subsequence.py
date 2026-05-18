# Is Subsequence (Easy)
# https://leetcode.com/problems/is-subsequence/
# Accepted 2026-05-18 — Python3, runtime 3 ms, memory 19.2 MB
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        

        sPointer=0

        for i in range(len(t)):
            if sPointer<len(s) and t[i]==s[sPointer]:
                sPointer+=1
            if sPointer>=len(s):
                return True

        return sPointer>=len(s)
