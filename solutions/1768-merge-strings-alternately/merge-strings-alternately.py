# Merge Strings Alternately (Easy)
# https://leetcode.com/problems/merge-strings-alternately/
# Accepted 2026-04-26 — Python3, runtime 49 ms, memory 19.1 MB
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        
        newStr=[]
        for i in range(max(len(word1), len(word2))):
            if i>len(word1)-1:
                newStr.append(word2[i])
            elif i>len(word2)-1:
                newStr.append(word1[i])
            else:
                newStr.append(word1[i])
                newStr.append(word2[i])

        return ''.join(newStr)
