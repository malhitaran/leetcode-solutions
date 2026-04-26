# Kids With the Greatest Number of Candies (Easy)
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Accepted 2026-04-26 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxCandy=max(candies)

        boolL=[]
        for candy in candies:
            if candy+extraCandies>=maxCandy:
                boolL.append(True)
            else:
                boolL.append(False)

        return boolL
