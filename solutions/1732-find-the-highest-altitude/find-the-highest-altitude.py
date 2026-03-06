# Find the Highest Altitude (Easy)
# https://leetcode.com/problems/find-the-highest-altitude/
# Accepted 2026-03-06 — Python3, runtime 0 ms, memory 19.2 MB
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt=0
        sumAlt=0
        for i in range(len(gain)):
            sumAlt+=gain[i]
            maxAlt=max(maxAlt, sumAlt)
        return maxAlt
