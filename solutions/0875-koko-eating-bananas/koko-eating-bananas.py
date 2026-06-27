# Koko Eating Bananas (Medium)
# https://leetcode.com/problems/koko-eating-bananas/
# Accepted 2026-06-27 — Python3, runtime 151 ms, memory 20.7 MB
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi=max(piles)
        lo=1
        best=0
        
        while lo<=hi:
            mid=((hi-lo)//2)+lo
            it=0
            for num in piles:
                it+=ceil(num/mid)
            if it<=h:
                best = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return best
