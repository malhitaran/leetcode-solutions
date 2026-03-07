# Unique Number of Occurrences (Easy)
# https://leetcode.com/problems/unique-number-of-occurrences/
# Accepted 2026-03-07 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        '''
        so we put all the numbers in different sets
        compare hte set sizes

        get the number of occurences and put that into a list, sets remove duplicates so comapre with set

        '''
        
        counts={}

        for num in arr:
            if num not in counts:
                counts[num]=1
            else:
                counts[num]+=1
        
        comp=list(counts.values())
        setComp=set(comp)

        if len(setComp)==len(comp):
            return True
        else:
            return False
