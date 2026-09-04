# Koko Eating Bananas (Medium)
# https://leetcode.com/problems/koko-eating-bananas/
# Accepted 2026-09-04 — Python3, runtime 183 ms, memory 20.5 MB
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        best=float('inf')

        l,r=1, max(piles)
        total=0
        while l<=r:
            total=0
            mid=(l+r)//2
            for pile in piles:
                total+=int(ceil(pile/mid))
            if total<=h:
                best=min(best, mid)
                r=mid-1
            else:
                l=mid+1

        return best
