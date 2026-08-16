# Group Anagrams (Medium)
# https://leetcode.com/problems/group-anagrams/
# Accepted 2026-08-16 — Python3, runtime 15 ms, memory 23.8 MB
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        '''
        store these in a frequency bucket

        buck -> list
        '''

        wordBucket=defaultdict(list)

        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            wordBucket[tuple(count)].append(word)

        return list(wordBucket.values())
