# Max Number of K-Sum Pairs (Medium)
# https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Accepted 2026-08-05 — Python3, runtime 473 ms, memory 32.3 MB
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        

        seen=defaultdict(int)
        ops=0
        for num in nums:

            if k-num in seen:
                ops+=1
                seen[k-num]-=1
                if seen[k-num]<=0:
                    seen.pop(k-num)
            else:
                seen[num]+=1 

        return ops
