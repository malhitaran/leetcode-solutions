# Merge Strings Alternately (Easy)
# https://leetcode.com/problems/merge-strings-alternately/
# Accepted 2025-09-09 — Python, runtime 14 ms, memory 12.6 MB
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=""
        i,j=0,0
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                merged+=word1[i]
                i+=1
            if j<len(word2):
                merged+=word2[j]
                j+=1
        return merged
