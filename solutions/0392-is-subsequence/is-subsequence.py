# Is Subsequence (Easy)
# https://leetcode.com/problems/is-subsequence/
# Accepted 2026-02-07 — Python3, runtime 0 ms, memory 19.3 MB
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while j<len(t) and i<len(s):
            if t[j]!=s[i]:
                j+=1
            else:
                i+=1
                j+=1

        if i==len(s):
            return True
        else:
            return False
