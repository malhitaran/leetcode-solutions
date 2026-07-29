# Kids With the Greatest Number of Candies (Easy)
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Accepted 2026-07-29 — Python3, runtime 0 ms, memory 19.3 MB
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        ourMax=max(candies)

        res=[]
        for number in candies:
            if extraCandies+number>=ourMax:
                res.append(True)
            else:
                res.append(False)

        return res
