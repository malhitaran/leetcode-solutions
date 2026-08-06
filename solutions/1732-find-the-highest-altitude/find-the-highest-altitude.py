# Find the Highest Altitude (Easy)
# https://leetcode.com/problems/find-the-highest-altitude/
# Accepted 2026-08-06 — Python3, runtime 0 ms, memory 19.2 MB
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        best, prevSum=0, 0


        for h in gain:

            prevSum+=h

            best=max(best, prevSum)

        return best
