# Koko Eating Bananas (Medium)
# https://leetcode.com/problems/koko-eating-bananas/
# Accepted 2026-08-14 — Python3, runtime 155 ms, memory 20.6 MB
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        '''
        okay so we have a array 

        [30,11,23,4,20]
        these are piles of bananas

        the first pile has 30 bananas

        the guards will come back in h hours

        how many bananas does koko need to eat the minimum

        need to find the minimum


        range of bananas 0-max

        [3,6,7,11]

        [0,1,2,3,4,5,6,7,8,9,10,11]


        print(start, 'start')
        print(end, 'end')
        print(mid, 'mid')
        print(temp, 'temp')
        print(best, 'best')
        '''
        
        
        '''
        for i in range(1, max(piles)+1):
            r.append(i)

        '''

        start,end=1, max(piles)
        best=end
        while start<=end:
            mid=(end+start)//2
            temp=0
            for pile in piles:
                temp+=ceil((pile )/(mid))
            if temp<=h:
                best=min(best, mid)
                end=mid-1
            else:
                start=mid+1
            
        return best
