# Can Place Flowers (Easy)
# https://leetcode.com/problems/can-place-flowers/
# Accepted 2026-05-16 — Python3, runtime 7 ms, memory 19.5 MB
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:


        '''

        [1,0,0,0,1]

        n=1


        2 cases


        its a 1 or its a 0

        for a 1 we just skip

        if its a zero we can cheeck previous and after and reduce n


        '''
        


        for i in range(len(flowerbed)):

            if flowerbed[i]==1:
                continue
            else:

                #start case
                if i==0 and len(flowerbed)>1:
                    if flowerbed[i+1]==0:
                        flowerbed[i]=1
                        n-=1
                #end case
                elif i ==len(flowerbed)-1:
                    if flowerbed[i-1]==0:
                        flowerbed[i]=1
                        n-=1
                elif flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                    flowerbed[i]=1
                    n-=1
        
        return n<=0
