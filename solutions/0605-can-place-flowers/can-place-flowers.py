# Can Place Flowers (Easy)
# https://leetcode.com/problems/can-place-flowers/
# Accepted 2026-05-16 — Python3, runtime 15 ms, memory 19.5 MB
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:


        '''

        cleaner solution

        '''
        for i in range(len(flowerbed)):
            left=(i==0)or(flowerbed[i-1]==0)
            right=(i==len(flowerbed)-1)or(flowerbed[i+1]==0)

            if flowerbed[i]==0 and left and right:
                flowerbed[i]=1
                n-=1

                if n==0:
                    return True

        return n<=0
