# Subarray Sum Equals K (Medium)
# https://leetcode.com/problems/subarray-sum-equals-k/
# Accepted 2026-07-07 — Python3, runtime 27 ms, memory 21.8 MB
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        subArrays=0
        pathSums={
            0:1
        }
        curSum=0

        for n in nums:
            curSum+=n
            subArrays+=pathSums.get(curSum-k,0)
            pathSums[curSum]=1+pathSums.get(curSum,0)

        return subArrays
