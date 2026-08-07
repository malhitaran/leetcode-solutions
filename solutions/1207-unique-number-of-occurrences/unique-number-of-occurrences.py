# Unique Number of Occurrences (Easy)
# https://leetcode.com/problems/unique-number-of-occurrences/
# Accepted 2026-08-07 — Python3, runtime 0 ms, memory 19.4 MB
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:


        numFreq=Counter(arr)
        ourCount=set()
    
        for freq in numFreq.values():
            if freq in ourCount:
                return False
            else:
                ourCount.add(freq)

        return True
