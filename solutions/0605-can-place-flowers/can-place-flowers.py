# Can Place Flowers (Easy)
# https://leetcode.com/problems/can-place-flowers/
# Accepted 2026-07-29 — Python3, runtime 23 ms, memory 19.8 MB
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        start=0
        end=len(flowerbed)-1
        for i in range(len(flowerbed)):
            
            #check left
            if flowerbed[i]==0:
                if (i==start or flowerbed[i-1]==0) and (i==end or flowerbed[i+1]==0):
                    n-=1
                    flowerbed[i]=1
                print(n)

        return n<=0
