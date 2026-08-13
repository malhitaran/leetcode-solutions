# Longest Repeating Character Replacement (Medium)
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Accepted 2026-08-13 — Python3, runtime 276 ms, memory 29.2 MB
from collections import defaultdict
import heapq
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        maybe we can see the most frequent character at any point 
        using a heap then doing a sliding window

        so basically we keep a dictionary then heapify it get the most common and and then keep a sum and then minus from teh sum
        '''
        
        ourDict=defaultdict(int)
        curS=0
        l=0
        heap=[]
        best=0
        for r in range(len(s)):
            curS+=1
            ourDict[s[r]]+=1
            heapq.heappush(heap, (-ourDict[s[r]], s[r]))

            
            while -heap[0][0] != ourDict[heap[0][1]]:
                heapq.heappop(heap)

            while curS-(-heap[0][0])>k:
                ourDict[s[l]]-=1
                curS-=1
                l+=1
                
                while -heap[0][0] != ourDict[heap[0][1]]:
                    heapq.heappop(heap)

            
            best=max(best, r-l+1)
        return best
