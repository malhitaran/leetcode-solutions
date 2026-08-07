# Determine if Two Strings Are Close (Medium)
# https://leetcode.com/problems/determine-if-two-strings-are-close/
# Accepted 2026-08-07 — Python3, runtime 75 ms, memory 20.4 MB
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1)!=len(word2):
            return False

        if set(word1) != set(word2):
            return False
        
        word1Freq=Counter(word1)
        word2Freq=Counter(word2)

        word1Freq=list(word1Freq.values())
        word2Freq=list(word2Freq.values())

        word1Freq.sort()
        word2Freq.sort()

        if word1Freq != word2Freq:
            print('here')
            return False
        return True
