# Kids With the Greatest Number of Candies (Easy)
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Accepted 2025-09-13 — Python3, runtime 0 ms, memory 17.7 MB
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolArray=[]

        max=0
        #finding max candies currently
        for i in candies:
            if i>max:
                max=i

        for i in candies:
            if i+extraCandies >= max:
                boolArray.append(True)
            else:
                boolArray.append(False)

        return boolArray
