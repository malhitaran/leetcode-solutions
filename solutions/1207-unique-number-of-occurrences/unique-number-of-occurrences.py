# Unique Number of Occurrences (Easy)
# https://leetcode.com/problems/unique-number-of-occurrences/
# Accepted 2026-03-07 — Python3, runtime 0 ms, memory 19.2 MB
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counts={}

        for num in arr:
            if num not in counts:
                counts[num]=1
            else:
                counts[num]+=1
        
        comp=list(counts.values())
        setComp=set(comp)

        return len(setComp) == len(comp)
