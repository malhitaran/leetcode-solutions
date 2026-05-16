# Kids With the Greatest Number of Candies (Easy)
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Accepted 2026-05-16 — Python3, runtime 0 ms, memory 19.2 MB
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        '''
        an O(n) solution
        '''

        boolArray=[]
        currMax=max(candies)

        
        for candy in candies:

            if candy+extraCandies>=currMax:
                boolArray.append(True)
            else:
                boolArray.append(False)

        return boolArray
