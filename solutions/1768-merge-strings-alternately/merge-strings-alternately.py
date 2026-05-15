# Merge Strings Alternately (Easy)
# https://leetcode.com/problems/merge-strings-alternately/
# Accepted 2026-05-15 — Python3, runtime 48 ms, memory 19.1 MB
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n=min(len(word1), len(word2))

        res=[]
        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])

        res.append(word1[n:])
        res.append(word2[n:])
    
        return ''.join(res)
