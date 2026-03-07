# Determine if Two Strings Are Close (Medium)
# https://leetcode.com/problems/determine-if-two-strings-are-close/
# Accepted 2026-03-07 — Python3, runtime 94 ms, memory 20.4 MB
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        '''
        case 1:compare lengths of word 1 and word2 if there equal and the sets of both are equal(contain the same stuff and no difference) that means both sets have the same letters(by sets) and the same amount of words(by len)

        case 2:get the occurences if the occurence is the same and the set of words are the same then its fine


        aaabc   
        iiias
        aabbbbcc
        bca
        cccab set occur
        aaacb

        '''

        count1=Counter(word1)
        count2=Counter(word2)

        return set(word1)==set(word2) and sorted(count1.values())==sorted(count2.values())
